from typing import List, Dict
from aiohttp import web

from openapi_server.models.found_users import FoundUsers
from openapi_server.models.page_bean_user import PageBeanUser
from openapi_server.models.page_bean_user_key import PageBeanUserKey
from openapi_server.models.user import User
from openapi_server import util


async def find_assignable_users(request: web.Request, query=None, session_id=None, username=None, account_id=None, project=None, issue_key=None, start_at=None, max_results=None, action_descriptor_id=None, recommend=None) -> web.Response:
    """Find users assignable to issues

    Returns a list of users that can be assigned to an issue. Use this operation to find the list of users who can be assigned to:   *  a new issue, by providing the &#x60;projectKeyOrId&#x60;.  *  an updated issue, by providing the &#x60;issueKey&#x60;.  *  to an issue during a transition (workflow action), by providing the &#x60;issueKey&#x60; and the transition id in &#x60;actionDescriptorId&#x60;. You can obtain the IDs of an issue&#39;s valid transitions using the &#x60;transitions&#x60; option in the &#x60;expand&#x60; parameter of [ Get issue](#api-rest-api-3-issue-issueIdOrKey-get).  In all these cases, you can pass an account ID to determine if a user can be assigned to an issue. The user is returned in the response if they can be assigned to the issue or issue transition.  This operation takes the users in the range defined by &#x60;startAt&#x60; and &#x60;maxResults&#x60;, up to the thousandth user, and then returns only the users from that range that can be assigned the issue. This means the operation usually returns fewer users than specified in &#x60;maxResults&#x60;. To get all the users who can be assigned the issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  Privacy controls are applied to the response based on the users&#39; preferences. This could mean, for example, that the user&#39;s email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param query: A query string that is matched against user attributes, such as &#x60;displayName&#x60;, and &#x60;emailAddress&#x60;, to find relevant users. The string can match the prefix of the attribute&#39;s value. For example, *query&#x3D;john* matches a user with a &#x60;displayName&#x60; of *John Smith* and a user with an &#x60;emailAddress&#x60; of *johnson@example.com*. Required, unless &#x60;username&#x60; or &#x60;accountId&#x60; is specified.
    :type query: str
    :param session_id: The sessionId of this request. SessionId is the same until the assignee is set.
    :type session_id: str
    :param username: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type username: str
    :param account_id: A query string that is matched exactly against user &#x60;accountId&#x60;. Required, unless &#x60;query&#x60; is specified.
    :type account_id: str
    :param project: The project ID or project key (case sensitive). Required, unless &#x60;issueKey&#x60; is specified.
    :type project: str
    :param issue_key: The key of the issue. Required, unless &#x60;project&#x60; is specified.
    :type issue_key: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return. This operation may return less than the maximum number of items even if more are available. The operation fetches users up to the maximum and then, from the fetched users, returns only the users that can be assigned to the issue.
    :type max_results: int
    :param action_descriptor_id: The ID of the transition.
    :type action_descriptor_id: int
    :param recommend: 
    :type recommend: bool

    """
    return web.Response(status=200)


async def find_bulk_assignable_users(request: web.Request, project_keys, query=None, username=None, account_id=None, start_at=None, max_results=None) -> web.Response:
    """Find users assignable to projects

    Returns a list of users who can be assigned issues in one or more projects. The list may be restricted to users whose attributes match a string.  This operation takes the users in the range defined by &#x60;startAt&#x60; and &#x60;maxResults&#x60;, up to the thousandth user, and then returns only the users from that range that can be assigned issues in the projects. This means the operation usually returns fewer users than specified in &#x60;maxResults&#x60;. To get all the users who can be assigned issues in the projects, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  Privacy controls are applied to the response based on the users&#39; preferences. This could mean, for example, that the user&#39;s email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

    :param project_keys: A list of project keys (case sensitive). This parameter accepts a comma-separated list.
    :type project_keys: str
    :param query: A query string that is matched against user attributes, such as &#x60;displayName&#x60; and &#x60;emailAddress&#x60;, to find relevant users. The string can match the prefix of the attribute&#39;s value. For example, *query&#x3D;john* matches a user with a &#x60;displayName&#x60; of *John Smith* and a user with an &#x60;emailAddress&#x60; of *johnson@example.com*. Required, unless &#x60;accountId&#x60; is specified.
    :type query: str
    :param username: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type username: str
    :param account_id: A query string that is matched exactly against user &#x60;accountId&#x60;. Required, unless &#x60;query&#x60; is specified.
    :type account_id: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def find_user_keys_by_query(request: web.Request, query, start_at=None, max_results=None) -> web.Response:
    """Find user keys by query

    Finds users with a structured query and returns a [paginated](#pagination) list of user keys.  This operation takes the users in the range defined by &#x60;startAt&#x60; and &#x60;maxResults&#x60;, up to the thousandth user, and then returns only the users from that range that match the structured query. This means the operation usually returns fewer users than specified in &#x60;maxResults&#x60;. To get all the users who match the structured query, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).  The query statements are:   *  &#x60;is assignee of PROJ&#x60; Returns the users that are assignees of at least one issue in project *PROJ*.  *  &#x60;is assignee of (PROJ-1, PROJ-2)&#x60; Returns users that are assignees on the issues *PROJ-1* or *PROJ-2*.  *  &#x60;is reporter of (PROJ-1, PROJ-2)&#x60; Returns users that are reporters on the issues *PROJ-1* or *PROJ-2*.  *  &#x60;is watcher of (PROJ-1, PROJ-2)&#x60; Returns users that are watchers on the issues *PROJ-1* or *PROJ-2*.  *  &#x60;is voter of (PROJ-1, PROJ-2)&#x60; Returns users that are voters on the issues *PROJ-1* or *PROJ-2*.  *  &#x60;is commenter of (PROJ-1, PROJ-2)&#x60; Returns users that have posted a comment on the issues *PROJ-1* or *PROJ-2*.  *  &#x60;is transitioner of (PROJ-1, PROJ-2)&#x60; Returns users that have performed a transition on issues *PROJ-1* or *PROJ-2*.  *  &#x60;[propertyKey].entity.property.path is \&quot;property value\&quot;&#x60; Returns users with the entity property value.  The list of issues can be extended as needed, as in *(PROJ-1, PROJ-2, ... PROJ-n)*. Statements can be combined using the &#x60;AND&#x60; and &#x60;OR&#x60; operators to form more complex queries. For example:  &#x60;is assignee of PROJ AND [propertyKey].entity.property.path is \&quot;property value\&quot;&#x60;

    :param query: The search query.
    :type query: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def find_users(request: web.Request, query=None, username=None, account_id=None, start_at=None, max_results=None, _property=None) -> web.Response:
    """Find users

    Returns a list of users that match the search string and property.  This operation first applies a filter to match the search string and property, and then takes the filtered users in the range defined by &#x60;startAt&#x60; and &#x60;maxResults&#x60;, up to the thousandth user. To get all the users who match the search string and property, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  This operation can be accessed anonymously.  Privacy controls are applied to the response based on the users&#39; preferences. This could mean, for example, that the user&#39;s email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls or calls by users without the required permission return empty search results.

    :param query: A query string that is matched against user attributes ( &#x60;displayName&#x60;, and &#x60;emailAddress&#x60;) to find relevant users. The string can match the prefix of the attribute&#39;s value. For example, *query&#x3D;john* matches a user with a &#x60;displayName&#x60; of *John Smith* and a user with an &#x60;emailAddress&#x60; of *johnson@example.com*. Required, unless &#x60;accountId&#x60; or &#x60;property&#x60; is specified.
    :type query: str
    :param username: 
    :type username: str
    :param account_id: A query string that is matched exactly against a user &#x60;accountId&#x60;. Required, unless &#x60;query&#x60; or &#x60;property&#x60; is specified.
    :type account_id: str
    :param start_at: The index of the first item to return in a page of filtered results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param _property: A query string used to search properties. Property keys are specified by path, so property keys containing dot (.) or equals (&#x3D;) characters cannot be used. The query string cannot be specified using a JSON object. Example: To search for the value of &#x60;nested&#x60; from &#x60;{\&quot;something\&quot;:{\&quot;nested\&quot;:1,\&quot;other\&quot;:2}}&#x60; use &#x60;thepropertykey.something.nested&#x3D;1&#x60;. Required, unless &#x60;accountId&#x60; or &#x60;query&#x60; is specified.
    :type _property: str

    """
    return web.Response(status=200)


async def find_users_by_query(request: web.Request, query, start_at=None, max_results=None) -> web.Response:
    """Find users by query

    Finds users with a structured query and returns a [paginated](#pagination) list of user details.  This operation takes the users in the range defined by &#x60;startAt&#x60; and &#x60;maxResults&#x60;, up to the thousandth user, and then returns only the users from that range that match the structured query. This means the operation usually returns fewer users than specified in &#x60;maxResults&#x60;. To get all the users who match the structured query, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).  The query statements are:   *  &#x60;is assignee of PROJ&#x60; Returns the users that are assignees of at least one issue in project *PROJ*.  *  &#x60;is assignee of (PROJ-1, PROJ-2)&#x60; Returns users that are assignees on the issues *PROJ-1* or *PROJ-2*.  *  &#x60;is reporter of (PROJ-1, PROJ-2)&#x60; Returns users that are reporters on the issues *PROJ-1* or *PROJ-2*.  *  &#x60;is watcher of (PROJ-1, PROJ-2)&#x60; Returns users that are watchers on the issues *PROJ-1* or *PROJ-2*.  *  &#x60;is voter of (PROJ-1, PROJ-2)&#x60; Returns users that are voters on the issues *PROJ-1* or *PROJ-2*.  *  &#x60;is commenter of (PROJ-1, PROJ-2)&#x60; Returns users that have posted a comment on the issues *PROJ-1* or *PROJ-2*.  *  &#x60;is transitioner of (PROJ-1, PROJ-2)&#x60; Returns users that have performed a transition on issues *PROJ-1* or *PROJ-2*.  *  &#x60;[propertyKey].entity.property.path is \&quot;property value\&quot;&#x60; Returns users with the entity property value.  The list of issues can be extended as needed, as in *(PROJ-1, PROJ-2, ... PROJ-n)*. Statements can be combined using the &#x60;AND&#x60; and &#x60;OR&#x60; operators to form more complex queries. For example:  &#x60;is assignee of PROJ AND [propertyKey].entity.property.path is \&quot;property value\&quot;&#x60;

    :param query: The search query.
    :type query: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def find_users_for_picker(request: web.Request, query, max_results=None, show_avatar=None, exclude=None, exclude_account_ids=None, avatar_size=None, exclude_connect_users=None) -> web.Response:
    """Find users for picker

    Returns a list of users whose attributes match the query term. The returned object includes the &#x60;html&#x60; field where the matched query term is highlighted with the HTML strong tag. A list of account IDs can be provided to exclude users from the results.  This operation takes the users in the range defined by &#x60;maxResults&#x60;, up to the thousandth user, and then returns only the users from that range that match the query term. This means the operation usually returns fewer users than specified in &#x60;maxResults&#x60;. To get all the users who match the query term, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  Privacy controls are applied to the response based on the users&#39; preferences. This could mean, for example, that the user&#39;s email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without the required permission return search results for an exact name match only.

    :param query: A query string that is matched against user attributes, such as &#x60;displayName&#x60;, and &#x60;emailAddress&#x60;, to find relevant users. The string can match the prefix of the attribute&#39;s value. For example, *query&#x3D;john* matches a user with a &#x60;displayName&#x60; of *John Smith* and a user with an &#x60;emailAddress&#x60; of *johnson@example.com*.
    :type query: str
    :param max_results: The maximum number of items to return. The total number of matched users is returned in &#x60;total&#x60;.
    :type max_results: int
    :param show_avatar: Include the URI to the user&#39;s avatar.
    :type show_avatar: bool
    :param exclude: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type exclude: List[str]
    :param exclude_account_ids: A list of account IDs to exclude from the search results. This parameter accepts a comma-separated list. Multiple account IDs can also be provided using an ampersand-separated list. For example, &#x60;excludeAccountIds&#x3D;5b10a2844c20165700ede21g,5b10a0effa615349cb016cd8&amp;excludeAccountIds&#x3D;5b10ac8d82e05b22cc7d4ef5&#x60;. Cannot be provided with &#x60;exclude&#x60;.
    :type exclude_account_ids: List[str]
    :param avatar_size: 
    :type avatar_size: str
    :param exclude_connect_users: 
    :type exclude_connect_users: bool

    """
    return web.Response(status=200)


async def find_users_with_all_permissions(request: web.Request, permissions, query=None, username=None, account_id=None, issue_key=None, project_key=None, start_at=None, max_results=None) -> web.Response:
    """Find users with permissions

    Returns a list of users who fulfill these criteria:   *  their user attributes match a search string.  *  they have a set of permissions for a project or issue.  If no search string is provided, a list of all users with the permissions is returned.  This operation takes the users in the range defined by &#x60;startAt&#x60; and &#x60;maxResults&#x60;, up to the thousandth user, and then returns only the users from that range that match the search string and have permission for the project or issue. This means the operation usually returns fewer users than specified in &#x60;maxResults&#x60;. To get all the users who match the search string and have permission for the project or issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  Privacy controls are applied to the response based on the users&#39; preferences. This could mean, for example, that the user&#39;s email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get users for any project.  *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project, to get users for that project.

    :param permissions: A comma separated list of permissions. Permissions can be specified as any:   *  permission returned by [Get all permissions](#api-rest-api-3-permissions-get).  *  custom project permission added by Connect apps.  *  (deprecated) one of the following:           *  ASSIGNABLE\\_USER      *  ASSIGN\\_ISSUE      *  ATTACHMENT\\_DELETE\\_ALL      *  ATTACHMENT\\_DELETE\\_OWN      *  BROWSE      *  CLOSE\\_ISSUE      *  COMMENT\\_DELETE\\_ALL      *  COMMENT\\_DELETE\\_OWN      *  COMMENT\\_EDIT\\_ALL      *  COMMENT\\_EDIT\\_OWN      *  COMMENT\\_ISSUE      *  CREATE\\_ATTACHMENT      *  CREATE\\_ISSUE      *  DELETE\\_ISSUE      *  EDIT\\_ISSUE      *  LINK\\_ISSUE      *  MANAGE\\_WATCHER\\_LIST      *  MODIFY\\_REPORTER      *  MOVE\\_ISSUE      *  PROJECT\\_ADMIN      *  RESOLVE\\_ISSUE      *  SCHEDULE\\_ISSUE      *  SET\\_ISSUE\\_SECURITY      *  TRANSITION\\_ISSUE      *  VIEW\\_VERSION\\_CONTROL      *  VIEW\\_VOTERS\\_AND\\_WATCHERS      *  VIEW\\_WORKFLOW\\_READONLY      *  WORKLOG\\_DELETE\\_ALL      *  WORKLOG\\_DELETE\\_OWN      *  WORKLOG\\_EDIT\\_ALL      *  WORKLOG\\_EDIT\\_OWN      *  WORK\\_ISSUE
    :type permissions: str
    :param query: A query string that is matched against user attributes, such as &#x60;displayName&#x60; and &#x60;emailAddress&#x60;, to find relevant users. The string can match the prefix of the attribute&#39;s value. For example, *query&#x3D;john* matches a user with a &#x60;displayName&#x60; of *John Smith* and a user with an &#x60;emailAddress&#x60; of *johnson@example.com*. Required, unless &#x60;accountId&#x60; is specified.
    :type query: str
    :param username: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type username: str
    :param account_id: A query string that is matched exactly against user &#x60;accountId&#x60;. Required, unless &#x60;query&#x60; is specified.
    :type account_id: str
    :param issue_key: The issue key for the issue.
    :type issue_key: str
    :param project_key: The project key for the project (case sensitive).
    :type project_key: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def find_users_with_browse_permission(request: web.Request, query=None, username=None, account_id=None, issue_key=None, project_key=None, start_at=None, max_results=None) -> web.Response:
    """Find users with browse permission

    Returns a list of users who fulfill these criteria:   *  their user attributes match a search string.  *  they have permission to browse issues.  Use this resource to find users who can browse:   *  an issue, by providing the &#x60;issueKey&#x60;.  *  any issue in a project, by providing the &#x60;projectKey&#x60;.  This operation takes the users in the range defined by &#x60;startAt&#x60; and &#x60;maxResults&#x60;, up to the thousandth user, and then returns only the users from that range that match the search string and have permission to browse issues. This means the operation usually returns fewer users than specified in &#x60;maxResults&#x60;. To get all the users who match the search string and have permission to browse issues, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  Privacy controls are applied to the response based on the users&#39; preferences. This could mean, for example, that the user&#39;s email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without the required permission return empty search results.

    :param query: A query string that is matched against user attributes, such as &#x60;displayName&#x60; and &#x60;emailAddress&#x60;, to find relevant users. The string can match the prefix of the attribute&#39;s value. For example, *query&#x3D;john* matches a user with a &#x60;displayName&#x60; of *John Smith* and a user with an &#x60;emailAddress&#x60; of *johnson@example.com*. Required, unless &#x60;accountId&#x60; is specified.
    :type query: str
    :param username: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type username: str
    :param account_id: A query string that is matched exactly against user &#x60;accountId&#x60;. Required, unless &#x60;query&#x60; is specified.
    :type account_id: str
    :param issue_key: The issue key for the issue. Required, unless &#x60;projectKey&#x60; is specified.
    :type issue_key: str
    :param project_key: The project key for the project (case sensitive). Required, unless &#x60;issueKey&#x60; is specified.
    :type project_key: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)
