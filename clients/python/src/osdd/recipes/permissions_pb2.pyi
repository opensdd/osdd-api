from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OperationPermission(_message.Message):
    __slots__ = ("bash", "read", "write")
    BASH_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    WRITE_FIELD_NUMBER: _ClassVar[int]
    bash: str
    read: str
    write: str
    def __init__(self, bash: _Optional[str] = ..., read: _Optional[str] = ..., write: _Optional[str] = ...) -> None: ...

class Permissions(_message.Message):
    __slots__ = ("allow", "deny")
    ALLOW_FIELD_NUMBER: _ClassVar[int]
    DENY_FIELD_NUMBER: _ClassVar[int]
    allow: _containers.RepeatedCompositeFieldContainer[OperationPermission]
    deny: _containers.RepeatedCompositeFieldContainer[OperationPermission]
    def __init__(self, allow: _Optional[_Iterable[_Union[OperationPermission, _Mapping]]] = ..., deny: _Optional[_Iterable[_Union[OperationPermission, _Mapping]]] = ...) -> None: ...
