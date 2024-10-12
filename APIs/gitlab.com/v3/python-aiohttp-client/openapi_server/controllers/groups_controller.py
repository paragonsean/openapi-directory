from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_requester import AccessRequester
from openapi_server.models.group import Group
from openapi_server.models.group_detail import GroupDetail
from openapi_server.models.issue import Issue
from openapi_server.models.member import Member
from openapi_server.models.notification_setting import NotificationSetting
from openapi_server.models.post_v3_groups_id_members_request import PostV3GroupsIdMembersRequest
from openapi_server.models.post_v3_groups_request import PostV3GroupsRequest
from openapi_server.models.project import Project
from openapi_server.models.put_v3_groups_id_access_requests_user_id_approve_request import PutV3GroupsIdAccessRequestsUserIdApproveRequest
from openapi_server.models.put_v3_groups_id_members_user_id_request import PutV3GroupsIdMembersUserIdRequest
from openapi_server.models.put_v3_groups_id_notification_settings_request import PutV3GroupsIdNotificationSettingsRequest
from openapi_server.models.put_v3_groups_id_request import PutV3GroupsIdRequest
from openapi_server import util


async def delete_v3_groups_id(request: web.Request, id) -> web.Response:
    """Remove a group.

    Remove a group.

    :param id: The ID of a group
    :type id: str

    """
    return web.Response(status=200)


async def delete_v3_groups_id_access_requests_user_id(request: web.Request, id, user_id) -> web.Response:
    """Denies an access request for the given user.

    This feature was introduced in GitLab 8.11.

    :param id: The group ID
    :type id: str
    :param user_id: The user ID of the access requester
    :type user_id: int

    """
    return web.Response(status=200)


async def delete_v3_groups_id_members_user_id(request: web.Request, id, user_id) -> web.Response:
    """Removes a user from a group or project.

    Removes a user from a group or project.

    :param id: The group ID
    :type id: str
    :param user_id: The user ID of the member
    :type user_id: int

    """
    return web.Response(status=200)


async def get_v3_groups(request: web.Request, statistics=None, all_available=None, search=None, order_by=None, sort=None, page=None, per_page=None, skip_groups=None) -> web.Response:
    """Get a groups list

    Get a groups list

    :param statistics: Include project statistics
    :type statistics: bool
    :param all_available: Show all group that you have access to
    :type all_available: bool
    :param search: Search for a specific group
    :type search: str
    :param order_by: Order by name or path
    :type order_by: str
    :param sort: Sort by asc (ascending) or desc (descending)
    :type sort: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int
    :param skip_groups: Array of group ids to exclude from list
    :type skip_groups: List[int]

    """
    return web.Response(status=200)


async def get_v3_groups_id(request: web.Request, id) -> web.Response:
    """Get a single group, with containing projects.

    Get a single group, with containing projects.

    :param id: The ID of a group
    :type id: str

    """
    return web.Response(status=200)


async def get_v3_groups_id_access_requests(request: web.Request, id, page=None, per_page=None) -> web.Response:
    """Gets a list of access requests for a group.

    This feature was introduced in GitLab 8.11.

    :param id: The group ID
    :type id: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_groups_id_issues(request: web.Request, id, state=None, labels=None, milestone=None, order_by=None, sort=None, page=None, per_page=None) -> web.Response:
    """Get a list of group issues

    Get a list of group issues

    :param id: The ID of a group
    :type id: str
    :param state: Return opened, closed, or all issues
    :type state: str
    :param labels: Comma-separated list of label names
    :type labels: str
    :param milestone: Return issues for a specific milestone
    :type milestone: str
    :param order_by: Return issues ordered by &#x60;created_at&#x60; or &#x60;updated_at&#x60; fields.
    :type order_by: str
    :param sort: Return issues sorted in &#x60;asc&#x60; or &#x60;desc&#x60; order.
    :type sort: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_groups_id_members(request: web.Request, id, query=None, page=None, per_page=None) -> web.Response:
    """Gets a list of group or project members viewable by the authenticated user.

    Gets a list of group or project members viewable by the authenticated user.

    :param id: The group ID
    :type id: str
    :param query: A query string to search for members
    :type query: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_groups_id_members_user_id(request: web.Request, id, user_id) -> web.Response:
    """Gets a member of a group or project.

    Gets a member of a group or project.

    :param id: The group ID
    :type id: str
    :param user_id: The user ID of the member
    :type user_id: int

    """
    return web.Response(status=200)


async def get_v3_groups_id_notification_settings(request: web.Request, id) -> web.Response:
    """Get group level notification level settings, defaults to Global

    This feature was introduced in GitLab 8.12

    :param id: The group ID or project ID or project NAMESPACE/PROJECT_NAME
    :type id: str

    """
    return web.Response(status=200)


async def get_v3_groups_id_projects(request: web.Request, id, archived=None, visibility=None, search=None, order_by=None, sort=None, simple=None, page=None, per_page=None) -> web.Response:
    """Get a list of projects in this group.

    Get a list of projects in this group.

    :param id: The ID of a group
    :type id: str
    :param archived: Limit by archived status
    :type archived: bool
    :param visibility: Limit by visibility
    :type visibility: str
    :param search: Return list of authorized projects matching the search criteria
    :type search: str
    :param order_by: Return projects ordered by field
    :type order_by: str
    :param sort: Return projects sorted in ascending and descending order
    :type sort: str
    :param simple: Return only the ID, URL, name, and path of each project
    :type simple: bool
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_groups_owned(request: web.Request, page=None, per_page=None, statistics=None) -> web.Response:
    """Get list of owned groups for authenticated user

    Get list of owned groups for authenticated user

    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int
    :param statistics: Include project statistics
    :type statistics: bool

    """
    return web.Response(status=200)


async def post_v3_groups(request: web.Request, body) -> web.Response:
    """Create a group. Available only for users who can create groups.

    Create a group. Available only for users who can create groups.

    :param body: 
    :type body: dict | bytes

    """
    body = PostV3GroupsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_groups_id_access_requests(request: web.Request, id) -> web.Response:
    """Requests access for the authenticated user to a group.

    This feature was introduced in GitLab 8.11.

    :param id: The group ID
    :type id: str

    """
    return web.Response(status=200)


async def post_v3_groups_id_members(request: web.Request, id, body) -> web.Response:
    """Adds a member to a group or project.

    Adds a member to a group or project.

    :param id: The group ID
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3GroupsIdMembersRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_groups_id_projects_project_id(request: web.Request, id, project_id) -> web.Response:
    """Transfer a project to the group namespace. Available only for admin.

    Transfer a project to the group namespace. Available only for admin.

    :param id: The ID of a group
    :type id: str
    :param project_id: The ID or path of the project
    :type project_id: str

    """
    return web.Response(status=200)


async def put_v3_groups_id(request: web.Request, id, body=None) -> web.Response:
    """Update a group. Available only for users who can administrate groups.

    Update a group. Available only for users who can administrate groups.

    :param id: The ID of a group
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3GroupsIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_groups_id_access_requests_user_id_approve(request: web.Request, id, user_id, body=None) -> web.Response:
    """Approves an access request for the given user.

    This feature was introduced in GitLab 8.11.

    :param id: The group ID
    :type id: str
    :param user_id: The user ID of the access requester
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3GroupsIdAccessRequestsUserIdApproveRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_groups_id_members_user_id(request: web.Request, id, user_id, body) -> web.Response:
    """Updates a member of a group or project.

    Updates a member of a group or project.

    :param id: The group ID
    :type id: str
    :param user_id: The user ID of the new member
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3GroupsIdMembersUserIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_groups_id_notification_settings(request: web.Request, id, body=None) -> web.Response:
    """Update group level notification level settings, defaults to Global

    This feature was introduced in GitLab 8.12

    :param id: The group ID or project ID or project NAMESPACE/PROJECT_NAME
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3GroupsIdNotificationSettingsRequest.from_dict(body)
    return web.Response(status=200)
