# Cattle DB

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Fast Time Series Database Implementation.

CattleDB can store timeseries data in typical cloud NoSQL databases.
At the moment Bigtable (GCP) and DynamoDB (AWS) storage backends are implemented.
Data can be queried by time ranges very efficiently.

CattleDB can be used as a library in projects or as a standalone service with a REST/gRPC backend to put/get data.

## Installation

Recursive option is needed to build the C speedups.

```sh
git clone --recursive https://github.com:smaxtec/cattledb.git
devenv shell
```

## Run tests against bigtable-emulator container

```sh
devenv shell
run-cattledb-tests
```

## Compile Python protobuf files

```sh
devenv shell
compile-protobuf-files
```

## Build cattledb container

```sh
devenv shell
build-cattledb-container
```

## Build container and run tests inside container manually

```sh
docker build . -t cattledb-test
docker run -it cattledb-test
service bigtable-server start
export BIGTABLE_EMULATOR_HOST="localhost:8080"
/app/.venv/bin/pytest tests -vv
```
