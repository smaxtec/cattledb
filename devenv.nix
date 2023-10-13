{ pkgs, ... }:

{
  env.GREET = "🐄 Welcome to the development environment for cattledb! 🐄";

  dotenv.disableHint = true;

  packages = with pkgs; [
    gcc
    cmake
    gnumake
    docker
  ];


  enterShell = ''
    # See [here](https://discourse.nixos.org/t/nixos-with-poetry-installed-pandas-libstdc-so-6-cannot-open-shared-object-file/8442/9) why this is needed
    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc
    ]}
    echo -e "\n$GREET\n"
  '';

  languages.python = {
    enable = true;
    version = "3.11";
    poetry = {
      enable = true;
      activate.enable = true;
      install = {
        enable = true;
        groups = [ "test" "protoc" "extensions" ];
      };
    };
  };

  pre-commit = {
    hooks = {
      autoflake.enable = true;
      black.enable = true;
      isort.enable = true;
    };
    settings = {
      autoflake.flags = "--in-place --remove-unused-variables --ignore-init-module-imports";
      # --remove-all-unused-imports";
    };
  };

  env = {
    "BIGTABLE_EMULATOR_HOST" = "localhost:8080";
  };

  scripts = {
    run-cattledb-tests.exec = ''
      docker compose -f docker/bigtable-emulator.yaml up -d
      pytest tests -vv
      docker compose -f docker/bigtable-emulator.yaml down
    '';
    build-cattledb-container.exec = ''
      docker compose -f docker/bigtable-emulator.yaml build
    '';
    compile-extensions.exec = ''
      cmake .
      make
    '';
    compile-protos.exec = ''
      python -m grpc.tools.protoc --python_out=./cattledb/grpcserver --grpc_python_out=./cattledb/grpcserver --proto_path=./protos cdb.proto
      sed -i "s/import cdb_pb2 as cdb__pb2/from . import cdb_pb2 as cdb__pb2/g" cattledb/grpcserver/cdb_pb2_grpc.py
    '';
  };
}
