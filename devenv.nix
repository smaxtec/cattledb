{ lib, pkgs, ... }:

{
  env.GREET = "🐄 Welcome to the development environment for cattledb! 🐄";

  dotenv.disableHint = true;

  enterShell = ''
    # See [here](https://discourse.nixos.org/t/nixos-with-poetry-installed-pandas-libstdc-so-6-cannot-open-shared-object-file/8442/9) why this is needed
    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc
    ]}
    echo -e "\n$GREET\n"
  '';

  languages.python = {
    enable = true;
    version = "3.10";
    poetry = {
      enable = true;
      activate.enable = true;
      install = {
        enable = true;
        groups = [ "test" "protoc" ];
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
      docker run -d --rm -p 8080:8080 --name=bigtable-emulator spotify/bigtable-emulator:latest
      pytest tests -vv
      docker stop bigtable-emulator
    '';
    build-cattledb-container.exec = ''
      docker build . -t cattledb-test
    '';
    compile-protobuf-files.exec = ''
      python -m grpc.tools.protoc --python_out=./cattledb/grpcserver --grpc_python_out=./cattledb/grpcserver --proto_path=./protos cdb.proto
      sed -i "s/import cdb_pb2 as cdb__pb2/from . import cdb_pb2 as cdb__pb2/g" cattledb/grpcserver/cdb_pb2_grpc.py
    '';
  };
}
