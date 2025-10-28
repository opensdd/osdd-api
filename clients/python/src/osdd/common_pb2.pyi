from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GitReference(_message.Message):
    __slots__ = ("path", "version")
    PATH_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    path: str
    version: GitVersion
    def __init__(self, path: _Optional[str] = ..., version: _Optional[_Union[GitVersion, _Mapping]] = ...) -> None: ...

class GitVersion(_message.Message):
    __slots__ = ("tag", "commit")
    TAG_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    tag: str
    commit: str
    def __init__(self, tag: _Optional[str] = ..., commit: _Optional[str] = ...) -> None: ...
