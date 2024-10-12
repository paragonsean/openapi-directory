from typing import List, Dict
from aiohttp import web

from openapi_server.models.group_get_default_response import GroupGetDefaultResponse
from openapi_server.models.group_user_create200_response import GroupUserCreate200Response
from openapi_server.models.group_user_list200_response import GroupUserList200Response
from openapi_server import util


async def group_user_create(request: web.Request, group_id, uid, api_version) -> web.Response:
    """group_user_create

    Adds a user to the specified group.

    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param uid: User identifier. Must be unique in the current API Management service instance.
    :type uid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def group_user_delete(request: web.Request, group_id, uid, api_version) -> web.Response:
    """group_user_delete

    Remove existing user from existing group.

    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param uid: User identifier. Must be unique in the current API Management service instance.
    :type uid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def group_user_list(request: web.Request, group_id, api_version, filter=None, top=None, skip=None) -> web.Response:
    """group_user_list

    Lists a collection of the members of the group, specified by its identifier.

    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: | Field            | Supported operators    | Supported functions               | |------------------|------------------------|-----------------------------------| | id               | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | firstName        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | lastName         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | email            | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state            | eq                     | N/A                               | | registrationDate | ge, le, eq, ne, gt, lt | N/A                               | | note             | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
