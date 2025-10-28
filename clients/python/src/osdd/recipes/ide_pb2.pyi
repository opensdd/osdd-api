from osdd import common_pb2 as _common_pb2
from osdd.recipes import permissions_pb2 as _permissions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ide(_message.Message):
    __slots__ = ("commands", "mcp", "permissions")
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    MCP_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    commands: Commands
    mcp: Mcp
    permissions: _permissions_pb2.Permissions
    def __init__(self, commands: _Optional[_Union[Commands, _Mapping]] = ..., mcp: _Optional[_Union[Mcp, _Mapping]] = ..., permissions: _Optional[_Union[_permissions_pb2.Permissions, _Mapping]] = ...) -> None: ...

class Mcp(_message.Message):
    __slots__ = ("servers",)
    class ServersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: McpServer
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[McpServer, _Mapping]] = ...) -> None: ...
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.MessageMap[str, McpServer]
    def __init__(self, servers: _Optional[_Mapping[str, McpServer]] = ...) -> None: ...

class McpServer(_message.Message):
    __slots__ = ("http", "stdio")
    HTTP_FIELD_NUMBER: _ClassVar[int]
    STDIO_FIELD_NUMBER: _ClassVar[int]
    http: HttpMcpServer
    stdio: StdioMcpServer
    def __init__(self, http: _Optional[_Union[HttpMcpServer, _Mapping]] = ..., stdio: _Optional[_Union[StdioMcpServer, _Mapping]] = ...) -> None: ...

class HttpMcpServer(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class StdioMcpServer(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: str
    def __init__(self, command: _Optional[str] = ...) -> None: ...

class Commands(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[Command]
    def __init__(self, entries: _Optional[_Iterable[_Union[Command, _Mapping]]] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ..., **kwargs) -> None: ...

class CommandFrom(_message.Message):
    __slots__ = ("github", "cmd", "text")
    GITHUB_FIELD_NUMBER: _ClassVar[int]
    CMD_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    github: _common_pb2.GitReference
    cmd: str
    text: str
    def __init__(self, github: _Optional[_Union[_common_pb2.GitReference, _Mapping]] = ..., cmd: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
