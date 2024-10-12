from typing import List, Dict
from aiohttp import web

from openapi_server.models.group_collection import GroupCollection
from openapi_server.models.group_contract import GroupContract
from openapi_server.models.group_create_parameters import GroupCreateParameters
from openapi_server.models.group_get_default_response import GroupGetDefaultResponse
from openapi_server.models.group_update_parameters import GroupUpdateParameters
from openapi_server import util


async def group_create_or_update(request: web.Request, group_id, api_version, parameters) -> web.Response:
    """group_create_or_update

    Creates or Updates a group.

    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Create parameters.
    :type parameters: dict | bytes

    """
    parameters = GroupCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def group_delete(request: web.Request, group_id, if_match, api_version) -> web.Response:
    """group_delete

    Deletes specific group of the API Management service instance.

    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param if_match: ETag of the Group Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def group_get(request: web.Request, group_id, api_version) -> web.Response:
    """group_get

    Gets the details of the group specified by its identifier.

    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def group_list(request: web.Request, api_version, filter=None, top=None, skip=None) -> web.Response:
    """group_list

    Lists a collection of groups defined within a service instance.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | type        | eq, ne                 | N/A                                         |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def group_update(request: web.Request, group_id, if_match, api_version, parameters) -> web.Response:
    """group_update

    Updates the details of the group specified by its identifier.

    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param if_match: ETag of the Group Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = GroupUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
