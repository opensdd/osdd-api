from osdd import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Prefetch(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[PrefetchEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[PrefetchEntry, _Mapping]]] = ...) -> None: ...

class PrefetchEntry(_message.Message):
    __slots__ = ("cmd",)
    CMD_FIELD_NUMBER: _ClassVar[int]
    cmd: _common_pb2.Exec
    def __init__(self, cmd: _Optional[_Union[_common_pb2.Exec, _Mapping]] = ...) -> None: ...

class PrefetchResult(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[FetchedData]
    def __init__(self, data: _Optional[_Iterable[_Union[FetchedData, _Mapping]]] = ...) -> None: ...

class FetchedData(_message.Message):
    __slots__ = ("id", "data")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    data: str
    def __init__(self, id: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...
