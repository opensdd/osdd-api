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
    __slots__ = ("path", "filter")
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    path: str
    filter: _common_pb2.EntryFilter
    def __init__(self, path: _Optional[str] = ..., filter: _Optional[_Union[_common_pb2.EntryFilter, _Mapping]] = ..., **kwargs) -> None: ...

class ContextFrom(_message.Message):
    __slots__ = ("combined", "github", "cmd", "text", "prefetch_id", "user_input", "local_file", "git_repo", "jira_issues", "linear_issues", "git_history", "url_fetch")
    COMBINED_FIELD_NUMBER: _ClassVar[int]
    GITHUB_FIELD_NUMBER: _ClassVar[int]
    CMD_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INPUT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FILE_FIELD_NUMBER: _ClassVar[int]
    GIT_REPO_FIELD_NUMBER: _ClassVar[int]
    JIRA_ISSUES_FIELD_NUMBER: _ClassVar[int]
    LINEAR_ISSUES_FIELD_NUMBER: _ClassVar[int]
    GIT_HISTORY_FIELD_NUMBER: _ClassVar[int]
    URL_FETCH_FIELD_NUMBER: _ClassVar[int]
    combined: CombinedContextSource
    github: _common_pb2.GitReference
    cmd: _common_pb2.Exec
    text: str
    prefetch_id: str
    user_input: UserInputContextSource
    local_file: str
    git_repo: _common_pb2.GitRepository
    jira_issues: JiraIssuesSource
    linear_issues: LinearIssuesSource
    git_history: GitHistorySource
    url_fetch: UrlSource
    def __init__(self, combined: _Optional[_Union[CombinedContextSource, _Mapping]] = ..., github: _Optional[_Union[_common_pb2.GitReference, _Mapping]] = ..., cmd: _Optional[_Union[_common_pb2.Exec, _Mapping]] = ..., text: _Optional[str] = ..., prefetch_id: _Optional[str] = ..., user_input: _Optional[_Union[UserInputContextSource, _Mapping]] = ..., local_file: _Optional[str] = ..., git_repo: _Optional[_Union[_common_pb2.GitRepository, _Mapping]] = ..., jira_issues: _Optional[_Union[JiraIssuesSource, _Mapping]] = ..., linear_issues: _Optional[_Union[LinearIssuesSource, _Mapping]] = ..., git_history: _Optional[_Union[GitHistorySource, _Mapping]] = ..., url_fetch: _Optional[_Union[UrlSource, _Mapping]] = ...) -> None: ...

class CombinedContextSource(_message.Message):
    __slots__ = ("items",)
    class Item(_message.Message):
        __slots__ = ("github", "cmd", "text", "prefetch_id", "user_input", "local_file")
        GITHUB_FIELD_NUMBER: _ClassVar[int]
        CMD_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        PREFETCH_ID_FIELD_NUMBER: _ClassVar[int]
        USER_INPUT_FIELD_NUMBER: _ClassVar[int]
        LOCAL_FILE_FIELD_NUMBER: _ClassVar[int]
        github: _common_pb2.GitReference
        cmd: _common_pb2.Exec
        text: str
        prefetch_id: str
        user_input: UserInputContextSource
        local_file: str
        def __init__(self, github: _Optional[_Union[_common_pb2.GitReference, _Mapping]] = ..., cmd: _Optional[_Union[_common_pb2.Exec, _Mapping]] = ..., text: _Optional[str] = ..., prefetch_id: _Optional[str] = ..., user_input: _Optional[_Union[UserInputContextSource, _Mapping]] = ..., local_file: _Optional[str] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CombinedContextSource.Item]
    def __init__(self, items: _Optional[_Iterable[_Union[CombinedContextSource.Item, _Mapping]]] = ...) -> None: ...

class UserInputContextSource(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[_common_pb2.UserInputParameter]
    def __init__(self, entries: _Optional[_Iterable[_Union[_common_pb2.UserInputParameter, _Mapping]]] = ...) -> None: ...

class JiraIssuesSource(_message.Message):
    __slots__ = ("site_id", "projects", "filter", "auth_token_env_var")
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_ENV_VAR_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    projects: _containers.RepeatedScalarFieldContainer[str]
    filter: IssuesFilter
    auth_token_env_var: str
    def __init__(self, site_id: _Optional[str] = ..., projects: _Optional[_Iterable[str]] = ..., filter: _Optional[_Union[IssuesFilter, _Mapping]] = ..., auth_token_env_var: _Optional[str] = ...) -> None: ...

class LinearIssuesSource(_message.Message):
    __slots__ = ("workspace", "teams", "filter", "auth_token_env_var")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_ENV_VAR_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    teams: _containers.RepeatedScalarFieldContainer[str]
    filter: IssuesFilter
    auth_token_env_var: str
    def __init__(self, workspace: _Optional[str] = ..., teams: _Optional[_Iterable[str]] = ..., filter: _Optional[_Union[IssuesFilter, _Mapping]] = ..., auth_token_env_var: _Optional[str] = ...) -> None: ...

class IssuesFilter(_message.Message):
    __slots__ = ("created_at_filter", "updated_at_filter")
    CREATED_AT_FILTER_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FILTER_FIELD_NUMBER: _ClassVar[int]
    created_at_filter: _common_pb2.DatesFilter
    updated_at_filter: _common_pb2.DatesFilter
    def __init__(self, created_at_filter: _Optional[_Union[_common_pb2.DatesFilter, _Mapping]] = ..., updated_at_filter: _Optional[_Union[_common_pb2.DatesFilter, _Mapping]] = ...) -> None: ...

class UrlSource(_message.Message):
    __slots__ = ("url", "optional")
    URL_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    url: str
    optional: bool
    def __init__(self, url: _Optional[str] = ..., optional: bool = ...) -> None: ...

class GitHistorySource(_message.Message):
    __slots__ = ("repo", "date_filter", "max_file_tokens", "skip_commits", "skip_prs", "commit_summary_only")
    REPO_FIELD_NUMBER: _ClassVar[int]
    DATE_FILTER_FIELD_NUMBER: _ClassVar[int]
    MAX_FILE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    SKIP_COMMITS_FIELD_NUMBER: _ClassVar[int]
    SKIP_PRS_FIELD_NUMBER: _ClassVar[int]
    COMMIT_SUMMARY_ONLY_FIELD_NUMBER: _ClassVar[int]
    repo: _common_pb2.GitRepository
    date_filter: _common_pb2.DatesFilter
    max_file_tokens: int
    skip_commits: bool
    skip_prs: bool
    commit_summary_only: bool
    def __init__(self, repo: _Optional[_Union[_common_pb2.GitRepository, _Mapping]] = ..., date_filter: _Optional[_Union[_common_pb2.DatesFilter, _Mapping]] = ..., max_file_tokens: _Optional[int] = ..., skip_commits: bool = ..., skip_prs: bool = ..., commit_summary_only: bool = ...) -> None: ...
