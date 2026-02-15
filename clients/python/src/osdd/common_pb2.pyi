from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GitReference(_message.Message):
    __slots__ = ("path", "version")
    PATH_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    path: str
    version: GitVersion
    def __init__(self, path: _Optional[str] = ..., version: _Optional[_Union[GitVersion, _Mapping]] = ...) -> None: ...

class GitRepository(_message.Message):
    __slots__ = ("full_name", "provider", "auth_token_env_var")
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_ENV_VAR_FIELD_NUMBER: _ClassVar[int]
    full_name: str
    provider: str
    auth_token_env_var: str
    def __init__(self, full_name: _Optional[str] = ..., provider: _Optional[str] = ..., auth_token_env_var: _Optional[str] = ...) -> None: ...

class GitVersion(_message.Message):
    __slots__ = ("tag", "commit")
    TAG_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    tag: str
    commit: str
    def __init__(self, tag: _Optional[str] = ..., commit: _Optional[str] = ...) -> None: ...

class UserInputParameter(_message.Message):
    __slots__ = ("name", "description", "optional", "text")
    class Text(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    optional: bool
    text: UserInputParameter.Text
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., optional: bool = ..., text: _Optional[_Union[UserInputParameter.Text, _Mapping]] = ...) -> None: ...

class NameGenConfig(_message.Message):
    __slots__ = ("len",)
    LEN_FIELD_NUMBER: _ClassVar[int]
    len: int
    def __init__(self, len: _Optional[int] = ...) -> None: ...

class Exec(_message.Message):
    __slots__ = ("cmd", "args")
    CMD_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    cmd: str
    args: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cmd: _Optional[str] = ..., args: _Optional[_Iterable[str]] = ...) -> None: ...

class EntryFilter(_message.Message):
    __slots__ = ("ide",)
    IDE_FIELD_NUMBER: _ClassVar[int]
    ide: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ide: _Optional[_Iterable[str]] = ...) -> None: ...
