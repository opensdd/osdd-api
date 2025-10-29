.PHONY: all clean proto-go proto-python proto-typescript install-deps generate test test-go

proto-go:
	@echo "Generating Go protobuf files..."
	@./scripts/generate-go.sh

proto-py:
	@echo "Generating Python protobuf files..."
	@./scripts/generate-py.sh

proto-ts:
	@echo "Generating TypeScript protobuf files..."
	@./scripts/generate-ts.sh


generate: proto-go proto-py proto-ts
  # all generated


test-go:
	@echo "Running Go tests..."
	@cd clients/go && go mod tidy && go test ./...

test: test-go
