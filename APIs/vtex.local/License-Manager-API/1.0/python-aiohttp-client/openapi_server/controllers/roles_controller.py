from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_user400_response import CreateUser400Response
from openapi_server.models.get_rolesby_user200_response_inner import GetRolesbyUser200ResponseInner
from openapi_server.models.get_user400_response import GetUser400Response
from openapi_server.models.list_roles_response import ListRolesResponse
from openapi_server import util


async def get_list_roles(request: web.Request, content_type, num_items=None, page_number=None, sort=None, sort_type=None) -> web.Response:
    """Get List of Roles

    Returns a list of available roles. The response is divided in pages. The query parameter &#x60;numItems&#x60; defines the number of items in each page, and consequently the amount of pages for the whole list.

    :param content_type: The media type of the body of the request. Default value for license manager protocol is application/json
    :type content_type: str
    :param num_items: Number of items in the returned page
    :type num_items: int
    :param page_number: Which page from the whole list will be returned
    :type page_number: int
    :param sort: Chooses the field that the list will be sorted by
    :type sort: str
    :param sort_type: Defines the sorting order. ASC is used for ascendant order. DSC is used for descendant order
    :type sort_type: str

    """
    return web.Response(status=200)


async def get_rolesby_user(request: web.Request, content_type, user_id) -> web.Response:
    """Get Roles by User/appKey

    Gets roles of a particular user or application key.

    :param content_type: The media type of the body of the request. Default value for license manager protocol is application/json
    :type content_type: str
    :param user_id: ID corresponding to the user
    :type user_id: str

    """
    return web.Response(status=200)


async def put_rolesin_user(request: web.Request, user_id, body) -> web.Response:
    """Put Roles in User/appKey

    Allows you to add roles to a particular user or application key by specifying the list of roles&#39; IDs on the request&#39;s body.

    :param user_id: ID corresponding to the user
    :type user_id: str
    :param body: List of roles&#39; IDs to add to the user or application key.
    :type body: List[int]

    """
    return web.Response(status=200)


async def remove_rolefrom_user(request: web.Request, content_type, user_id, role_id) -> web.Response:
    """Remove Role from User/appKey

    Allows you to remove a role from a specific user or application key. This method only allows the removal of one role per request. The role&#39;s ID must be specified on the request path, not on the request body.    &gt; Note that a successful response returns a &#x60;204&#x60; response with an empty body. A deletion on a role or user that does not exist will also return a &#x60;204&#x60;. Thus, this method should not be used to verify the existence of a specific user or role.

    :param content_type: The media type of the body of the request. Default value for license manager protocol is application/json
    :type content_type: str
    :param user_id: ID corresponding to the user
    :type user_id: str
    :param role_id: ID of the role which will be removed from the user
    :type role_id: str

    """
    return web.Response(status=200)
