from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_group_meta_data import CreateGroupMetaData
from openapi_server.models.error import Error
from openapi_server.models.group_meta_data import GroupMetaData
from openapi_server.models.group_search_results import GroupSearchResults
from openapi_server.models.sort_by import SortBy
from openapi_server.models.sort_order import SortOrder
from openapi_server import util


async def create_group(request: web.Request, body) -> web.Response:
    """Create a new group

    Creates a new group.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) * The group already exist (HTTP error &#x60;409&#x60;) 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateGroupMetaData.from_dict(body)
    return web.Response(status=200)


async def delete_group_by_id(request: web.Request, group_id) -> web.Response:
    """Delete a group by the specified ID.

    Deletes a group by identifier.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) * The group does not exist (HTTP error &#x60;404&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str

    """
    return web.Response(status=200)


async def get_group_by_id(request: web.Request, group_id) -> web.Response:
    """Get a group by the specified ID.

    Returns a group using the specified id.  This operation can fail for the following reasons:  * No group exists with the specified ID (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str

    """
    return web.Response(status=200)


async def list_groups(request: web.Request, limit=None, offset=None, order=None, orderby=None) -> web.Response:
    """List groups

    Returns a list of all groups.  This list is paged.

    :param limit: The number of groups to return.  Defaults to 20.
    :type limit: int
    :param offset: The number of groups to skip before starting the result set.  Defaults to 0.
    :type offset: int
    :param order: Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;).
    :type order: dict | bytes
    :param orderby: The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60; 
    :type orderby: dict | bytes

    """
    order = .from_dict(order)
    orderby = .from_dict(orderby)
    return web.Response(status=200)
