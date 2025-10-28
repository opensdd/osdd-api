#!/usr/bin/env bash

set -ex
set -o pipefail

root=$(git rev-parse --show-toplevel)

echo "Generating Python protobuf files..."

PROTO_FILES=$(find protos -name "*.proto" | sed 's|^protos/||')

py_root="$root"/clients/python

uv --directory "$py_root" sync

uv --directory "$py_root" run python -m grpc_tools.protoc \
  -I "${root}/protos"  \
  --python_out=./src/ \
  --pyi_out=./src/ \
  --experimental_allow_proto3_optional \
  ${PROTO_FILES}

find "$py_root"/src/osdd/ -type d -exec touch {}/__init__.py \;
