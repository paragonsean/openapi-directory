from typing import List, Dict
from aiohttp import web

from openapi_server.models.property_collection import PropertyCollection
from openapi_server.models.property_contract import PropertyContract
from openapi_server.models.property_get_default_response import PropertyGetDefaultResponse
from openapi_server.models.property_update_parameters import PropertyUpdateParameters
from openapi_server import util


async def property_create_or_update(request: web.Request, prop_id, api_version, parameters) -> web.Response:
    """property_create_or_update

    Creates or updates a property.

    :param prop_id: Identifier of the property.
    :type prop_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Create parameters.
    :type parameters: dict | bytes

    """
    parameters = PropertyContract.from_dict(parameters)
    return web.Response(status=200)


async def property_delete(request: web.Request, prop_id, if_match, api_version) -> web.Response:
    """property_delete

    Deletes specific property from the API Management service instance.

    :param prop_id: Identifier of the property.
    :type prop_id: str
    :param if_match: The entity state (Etag) version of the property to delete. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def property_get(request: web.Request, prop_id, api_version) -> web.Response:
    """property_get

    Gets the details of the property specified by its identifier.

    :param prop_id: Identifier of the property.
    :type prop_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def property_list(request: web.Request, api_version, filter=None, top=None, skip=None) -> web.Response:
    """property_list

    Lists a collection of properties defined within a service instance.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: | Field | Supported operators    | Supported functions                                   | |-------|------------------------|-------------------------------------------------------| | tags  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith, any, all | | name  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith           |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def property_update(request: web.Request, prop_id, if_match, api_version, parameters) -> web.Response:
    """property_update

    Updates the specific property.

    :param prop_id: Identifier of the property.
    :type prop_id: str
    :param if_match: The entity state (Etag) version of the property to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = PropertyUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
