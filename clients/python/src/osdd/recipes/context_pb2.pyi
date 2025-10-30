from osdd import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Context(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[ContextEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[ContextEntry, _Mapping]]] = ...) -> None: ...

class ContextEntry(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ..., **kwargs) -> None: ...

class ContextFrom(_message.Message):
    __slots__ = ("combined", "github", "cmd", "text", "prefetch_id", "user_input")
    COMBINED_FIELD_NUMBER: _ClassVar[int]
    GITHUB_FIELD_NUMBER: _ClassVar[int]
    CMD_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INPUT_FIELD_NUMBER: _ClassVar[int]
    combined: CombinedContextSource
    github: _common_pb2.GitReference
    cmd: _common_pb2.Exec
    text: str
    prefetch_id: str
    user_input: UserInputContextSource
    def __init__(self, combined: _Optional[_Union[CombinedContextSource, _Mapping]] = ..., github: _Optional[_Union[_common_pb2.GitReference, _Mapping]] = ..., cmd: _Optional[_Union[_common_pb2.Exec, _Mapping]] = ..., text: _Optional[str] = ..., prefetch_id: _Optional[str] = ..., user_input: _Optional[_Union[UserInputContextSource, _Mapping]] = ...) -> None: ...

class CombinedContextSource(_message.Message):
    __slots__ = ("items",)
    class Item(_message.Message):
        __slots__ = ("github", "cmd", "text", "prefetch_id", "user_input")
        GITHUB_FIELD_NUMBER: _ClassVar[int]
        CMD_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        PREFETCH_ID_FIELD_NUMBER: _ClassVar[int]
        USER_INPUT_FIELD_NUMBER: _ClassVar[int]
        github: _common_pb2.GitReference
        cmd: _common_pb2.Exec
        text: str
        prefetch_id: str
        user_input: UserInputContextSource
        def __init__(self, github: _Optional[_Union[_common_pb2.GitReference, _Mapping]] = ..., cmd: _Optional[_Union[_common_pb2.Exec, _Mapping]] = ..., text: _Optional[str] = ..., prefetch_id: _Optional[str] = ..., user_input: _Optional[_Union[UserInputContextSource, _Mapping]] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CombinedContextSource.Item]
    def __init__(self, items: _Optional[_Iterable[_Union[CombinedContextSource.Item, _Mapping]]] = ...) -> None: ...

class UserInputContextSource(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[_common_pb2.UserInputParameter]
    def __init__(self, entries: _Optional[_Iterable[_Union[_common_pb2.UserInputParameter, _Mapping]]] = ...) -> None: ...
