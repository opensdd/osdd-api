// Public API: export only symbols declared in proto files (no DeepPartial, MessageFns, etc.)

// osdd.common
export { GitReference, GitVersion, protobufPackage as common_protobufPackage } from './osdd/common';

// osdd.context
export {
  Context,
  ContextEntry,
  ContextFrom,
  CombinedContextSource,
  CombinedContextSource_Item,
  protobufPackage as context_protobufPackage,
} from './osdd/recipes/context';

// osdd.ide
export {
  Ide,
  Mcp,
  Mcp_ServersEntry,
  McpServer,
  HttpMcpServer,
  StdioMcpServer,
  Commands,
  Command,
  CommandFrom,
  protobufPackage as ide_protobufPackage,
} from './osdd/recipes/ide';

// osdd.permissions
export {
  OperationPermission,
  Permissions,
  protobufPackage as permissions_protobufPackage,
} from './osdd/recipes/permissions';

export {
  Recipe,
  protobufPackage as recipe_protobufPackage,
} from './osdd/recipes/recipe';

export {
  Prefetch,
  PrefetchEntry,
  PrefetchResult,
  FetchedData,
  protobufPackage as content_protobufPackage,
} from './osdd/content';
