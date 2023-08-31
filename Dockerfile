# -*- docker-image-name: "spotify/bigtable-emulator" -*-
FROM spotify/bigtable-emulator as emu

RUN ls /go

FROM python:3.10

# Copy Go runtime and service from other container
COPY --from=emu /go /go
COPY bigtable-emu/bigtable-server /etc/init.d/bigtable-server
RUN  chmod 700 /etc/init.d/bigtable-server

RUN apt-get update
RUN apt-get install -y ca-certificates

RUN mkdir -p /app
WORKDIR /app

# This should be set to the same version as poetry-core in pyproject.toml
ENV POETRY_VERSION=1.5.1

# Update pip and install the same version as
# poetry-core in pyproject.toml
RUN pip install -U pip setuptools
RUN pip install poetry==${POETRY_VERSION}

# Install dependencies with poetry
COPY . /app
RUN poetry config virtualenvs.create false

ARG mode

RUN poetry install --with test

CMD ["bash"]
