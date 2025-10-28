#!/usr/bin/env bash

set -ex
set -o pipefail

root=$(git rev-parse --show-toplevel)

echo "Generating TypeScript protobuf files..."

PROTO_FILES=$(find protos -name "*.proto" | sed 's|^protos/||')

ts_root="$root"/clients/ts

cd "$ts_root"
npm install
cd "$root"

protoc \
  -I "${root}/protos"  \
  --plugin="$ts_root"/node_modules/.bin/protoc-gen-ts_proto \
  --ts_proto_out="$ts_root/src" \
  --ts_proto_opt=globalThisPolyfill=true,unrecognizedEnum=false,oneof=unions-value,outputServices=nice-grpc,outputServices=generic-definitions,useExactTypes=false \
  ${PROTO_FILES}
