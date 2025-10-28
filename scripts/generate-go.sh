#!/usr/bin/env bash

set -ex
set -o pipefail

root=$(git rev-parse --show-toplevel)

echo "Generating Go protobuf files..."

go_root="$root"/clients/go
export GOBIN="$go_root/bin"
mkdir -p "$GOBIN"

cd "$go_root"
go mod download
go install google.golang.org/protobuf/cmd/protoc-gen-go
cd "$root"

PROTO_FILES=$(find protos -name "*.proto" | sed 's|^protos/||')

protoc \
  -I "${root}/protos"  \
  --proto_path=. \
  --plugin="$GOBIN"/protoc-gen-go \
  --go_out="$root" \
  --go_opt=default_api_level=API_OPAQUE,paths=import \
  --go_opt=module=github.com/opensdd/osdd-api \
  ${PROTO_FILES}
