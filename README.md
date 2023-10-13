# Cattle DB

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Fast Time Series Database Implementation.

CattleDB can store timeseries data in typical cloud NoSQL databases.
At the moment Bigtable (GCP) and DynamoDB (AWS) storage backends are implemented.
Data can be queried by time ranges very efficiently.

CattleDB can be used as a library in projects or as a standalone service with a REST/gRPC backend to put/get data.

## Installation

To use the development environment you have to have [Nix](https://nixos.org/download#download-nix) and [devenv](https://devenv.sh/) installed.

```sh
git clone https://github.com:smaxtec/cattledb.git
devenv shell
```

## Run tests against bigtable-emulator container

```sh
devenv shell
run-cattledb-tests
```

## Compile Python protobuf files

The files reside in the `protos` directory.

```sh
devenv shell
compile-protos
```

The files reside in the `extensions` directory.
They originate from the [cattledb-extensions repository](https://github.com/smaxtec/cattledb-extensions).

## Compile C++ extensions

The files reside in the `extensions` directory.

```sh
devenv shell
compile-extensions
```

## Build cattledb container

```sh
devenv shell
build-cattledb-container
```

## Using cbt to access Bigtable

Launch Bigtable emulator.

```sh
docker compose -f docker/bigtable-emulator.yaml up -d
```

Inside the Docker container, the Google Cloud Bigtable Tool `cbt` is installed.
With it, you can modify data on tables created on the Bigtable emulator.

For a list of available commands, take a look at the [cbt CLI reference](https://cloud.google.com/bigtable/docs/cbt-reference).

If one wishes to install the tool locally, you can find more information [here](https://cloud.google.com/bigtable/docs/cbt-overview).

The tool can also be built from source available [here](https://github.com/googleapis/cloud-bigtable-cbt-cli).
