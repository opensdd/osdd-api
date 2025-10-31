from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MaterializedResult(_message.Message):
    __slots__ = ("entries",)
    class Entry(_message.Message):
        __slots__ = ("file", "directory")
        FILE_FIELD_NUMBER: _ClassVar[int]
        DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        file: FullFileContent
        directory: str
        def __init__(self, file: _Optional[_Union[FullFileContent, _Mapping]] = ..., directory: _Optional[str] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[MaterializedResult.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[MaterializedResult.Entry, _Mapping]]] = ...) -> None: ...

class FullFileContent(_message.Message):
    __slots__ = ("path", "content")
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: str
    def __init__(self, path: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
