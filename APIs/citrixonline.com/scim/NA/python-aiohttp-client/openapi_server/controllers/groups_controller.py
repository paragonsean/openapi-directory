from typing import List, Dict
from aiohttp import web

from openapi_server.models.group import Group
from openapi_server.models.group_collection import GroupCollection
from openapi_server.models.group_definition import GroupDefinition
from openapi_server import util


async def create_group(request: web.Request, authorization, body) -> web.Response:
    """Create Group

    Creates a new organization group and adds it to the user domain. Member groups and member users must be in the organization. This call requires the role ROLE_ORG_WRITE.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param body: The details of the group to create
    :type body: dict | bytes

    """
    body = GroupDefinition.from_dict(body)
    return web.Response(status=200)


async def delete_group(request: web.Request, authorization, group_key) -> web.Response:
    """Delete Group

    Deletes a group from the organization (but not from the account). The group must be in the organization. This call requires the role ROLE_ORG_WRITE.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param group_key: The key of the group to query. The group must be in the organization domain
    :type group_key: int

    """
    return web.Response(status=200)


async def get_group(request: web.Request, authorization, group_key) -> web.Response:
    """Get Group

    Queries group details in the organization domain. This call requires the role ROLE_ORG_READ.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param group_key: The key of the group to query. The group must be in the organization domain
    :type group_key: int

    """
    return web.Response(status=200)


async def get_groups(request: web.Request, authorization, filter=None) -> web.Response:
    """Get Groups

    Queries multiple group identities in the organization domain. Filtering, sorting and pagination are available. This call requires the role ROLE_ORG_READ.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param filter:  Without a filter, all groups are returned. The filter parameter must be a properly formed SCIM filter using the operator \&quot;eq\&quot; (equals), \&quot;sw\&quot; (starts with), or \&quot;co\&quot; (contains). The filter works for the displayName attribute. Sorting and pagination are supported. For example, GET /Groups?filter&#x3D;displayName%20eq%20%22Engineering%22&amp;sortBy&#x3D;displayName&amp;sortOrder&#x3D;ascending&amp;count&#x3D;50&amp;startIndex&#x3D;51
    :type filter: str

    """
    return web.Response(status=200)


async def replace_group(request: web.Request, authorization, group_key, body) -> web.Response:
    """Replace Group

    Updates an existing group. The request must include the full group definition. To modify one or more values without sending the full definition, see \&quot;Update Group\&quot;. Member groups and member users must be in the organization. This call requires the role ROLE_ORG_WRITE.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param group_key: The key of the group to query. The group must be in the organization domain
    :type group_key: int
    :param body: The new group definition
    :type body: dict | bytes

    """
    body = GroupDefinition.from_dict(body)
    return web.Response(status=200)


async def update_group(request: web.Request, authorization, group_key, body) -> web.Response:
    """Update Group

    Updates one or more values of an existing group without sending the full definition. Member groups and member users must be in the organization. This call requires the role ROLE_ORG_WRITE.

    :param authorization: Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39;
    :type authorization: str
    :param group_key: The key of the group to query. The group must be in the organization domain
    :type group_key: int
    :param body: The group data to update. It is allowed to update one or more values of the group definition
    :type body: dict | bytes

    """
    body = GroupDefinition.from_dict(body)
    return web.Response(status=200)
