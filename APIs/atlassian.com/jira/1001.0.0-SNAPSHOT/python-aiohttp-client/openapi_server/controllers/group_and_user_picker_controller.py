from typing import List, Dict
from aiohttp import web

from openapi_server.models.found_users_and_groups import FoundUsersAndGroups
from openapi_server import util


async def find_users_and_groups(request: web.Request, query, max_results=None, show_avatar=None, field_id=None, project_id=None, issue_type_id=None, avatar_size=None, case_insensitive=None, exclude_connect_addons=None) -> web.Response:
    """Find users and groups

    Returns a list of users and groups matching a string. The string is used:   *  for users, to find a case-insensitive match with display name and e-mail address. Note that if a user has hidden their email address in their user profile, partial matches of the email address will not find the user. An exact match is required.  *  for groups, to find a case-sensitive match with group name.  For example, if the string *tin* is used, records with the display name *Tina*, email address *sarah@tinplatetraining.com*, and the group *accounting* would be returned.  Optionally, the search can be refined to:   *  the projects and issue types associated with a custom field, such as a user picker. The search can then be further refined to return only users and groups that have permission to view specific:           *  projects.      *  issue types.          If multiple projects or issue types are specified, they must be a subset of those enabled for the custom field or no results are returned. For example, if a field is enabled for projects A, B, and C then the search could be limited to projects B and C. However, if the search is limited to projects B and D, nothing is returned.  *  not return Connect app users and groups.  *  return groups that have a case-insensitive match with the query.  The primary use case for this resource is to populate a picker field suggestion list with users or groups. To this end, the returned object includes an &#x60;html&#x60; field for each list. This field highlights the matched query term in the item name with the HTML strong tag. Also, each list is wrapped in a response object that contains a header for use in a picker, specifically *Showing X of Y matching groups*.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/yodKLg).

    :param query: The search string.
    :type query: str
    :param max_results: The maximum number of items to return in each list.
    :type max_results: int
    :param show_avatar: Whether the user avatar should be returned. If an invalid value is provided, the default value is used.
    :type show_avatar: bool
    :param field_id: The custom field ID of the field this request is for.
    :type field_id: str
    :param project_id: The ID of a project that returned users and groups must have permission to view. To include multiple projects, provide an ampersand-separated list. For example, &#x60;projectId&#x3D;10000&amp;projectId&#x3D;10001&#x60;. This parameter is only used when &#x60;fieldId&#x60; is present.
    :type project_id: List[str]
    :param issue_type_id: The ID of an issue type that returned users and groups must have permission to view. To include multiple issue types, provide an ampersand-separated list. For example, &#x60;issueTypeId&#x3D;10000&amp;issueTypeId&#x3D;10001&#x60;. Special values, such as &#x60;-1&#x60; (all standard issue types) and &#x60;-2&#x60; (all subtask issue types), are supported. This parameter is only used when &#x60;fieldId&#x60; is present.
    :type issue_type_id: List[str]
    :param avatar_size: The size of the avatar to return. If an invalid value is provided, the default value is used.
    :type avatar_size: str
    :param case_insensitive: Whether the search for groups should be case insensitive.
    :type case_insensitive: bool
    :param exclude_connect_addons: Whether Connect app users and groups should be excluded from the search results. If an invalid value is provided, the default value is used.
    :type exclude_connect_addons: bool

    """
    return web.Response(status=200)
