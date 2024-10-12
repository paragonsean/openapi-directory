from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_group_request import CreateGroupRequest
from openapi_server.models.group import Group
from openapi_server.models.legacy_error import LegacyError
from openapi_server import util


async def create_group(request: web.Request, body) -> web.Response:
    """Create a group

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_group(request: web.Request, group_id) -> web.Response:
    """Delete a group

    

    :param group_id: The ID of the group.
    :type group_id: 

    """
    return web.Response(status=200)


async def get_group(request: web.Request, group_id) -> web.Response:
    """Get a specific group

    

    :param group_id: The ID of the group.
    :type group_id: 

    """
    return web.Response(status=200)


async def get_groups(request: web.Request, direction=None, filter=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all groups

    

    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.  Option descriptions:  * &#x60;relevant&#x60; - Relevant sorting is available only for search queries. 
    :type sort: str

    """
    return web.Response(status=200)
