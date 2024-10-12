from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_group_request import CreateGroupRequest
from openapi_server.models.create_group_response import CreateGroupResponse
from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_group_response import FetchGroupResponse
from openapi_server.models.fetch_groups_response import FetchGroupsResponse
from openapi_server import util


async def create_group(request: web.Request, body) -> web.Response:
    """Create a group

    Create a group record.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateGroupRequest.from_dict(body)
    return web.Response(status=200)


async def fetch_group(request: web.Request, id) -> web.Response:
    """Get a group

    Get a group record by id.

    :param id: Group identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_groups(request: web.Request, filter_organization, filter_name=None) -> web.Response:
    """List groups

    Get a list of groups matching the specified filters.

    :param filter_organization: Organization identifier
    :type filter_organization: str
    :param filter_name: Group name
    :type filter_name: str

    """
    return web.Response(status=200)
