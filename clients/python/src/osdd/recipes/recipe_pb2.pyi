from osdd.recipes import context_pb2 as _context_pb2
from osdd.recipes import ide_pb2 as _ide_pb2
from osdd import content_pb2 as _content_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Recipe(_message.Message):
    __slots__ = ("prefetch", "context", "ide")
    PREFETCH_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IDE_FIELD_NUMBER: _ClassVar[int]
    prefetch: _content_pb2.Prefetch
    context: _context_pb2.Context
    ide: _ide_pb2.Ide
    def __init__(self, prefetch: _Optional[_Union[_content_pb2.Prefetch, _Mapping]] = ..., context: _Optional[_Union[_context_pb2.Context, _Mapping]] = ..., ide: _Optional[_Union[_ide_pb2.Ide, _Mapping]] = ...) -> None: ...

class ExecutableRecipe(_message.Message):
    __slots__ = ("recipe", "entry_point")
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_POINT_FIELD_NUMBER: _ClassVar[int]
    recipe: Recipe
    entry_point: EntryPoint
    def __init__(self, recipe: _Optional[_Union[Recipe, _Mapping]] = ..., entry_point: _Optional[_Union[EntryPoint, _Mapping]] = ...) -> None: ...

class EntryPoint(_message.Message):
    __slots__ = ("ide_type", "start")
    IDE_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    ide_type: str
    start: StartConfig
    def __init__(self, ide_type: _Optional[str] = ..., start: _Optional[_Union[StartConfig, _Mapping]] = ...) -> None: ...

class StartConfig(_message.Message):
    __slots__ = ("command", "prompt")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    command: str
    prompt: str
    def __init__(self, command: _Optional[str] = ..., prompt: _Optional[str] = ...) -> None: ...
