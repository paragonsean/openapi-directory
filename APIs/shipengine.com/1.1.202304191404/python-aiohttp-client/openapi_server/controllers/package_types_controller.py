from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_package_type_request_body import CreatePackageTypeRequestBody
from openapi_server.models.create_package_type_response_body import CreatePackageTypeResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_package_type_by_id_response_body import GetPackageTypeByIdResponseBody
from openapi_server.models.list_package_types_response_body import ListPackageTypesResponseBody
from openapi_server.models.update_package_type_request_body import UpdatePackageTypeRequestBody
from openapi_server import util


async def create_package_type(request: web.Request, body) -> web.Response:
    """Create Custom Package Type

    Create a custom package type to better assist in getting accurate rate estimates

    :param body: 
    :type body: dict | bytes

    """
    body = CreatePackageTypeRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_package_type(request: web.Request, package_id) -> web.Response:
    """Delete A Custom Package By ID

    Delete a custom package using the ID

    :param package_id: Package ID
    :type package_id: str

    """
    return web.Response(status=200)


async def get_package_type_by_id(request: web.Request, package_id) -> web.Response:
    """Get Custom Package Type By ID

    Get Custom Package Type by ID

    :param package_id: Package ID
    :type package_id: str

    """
    return web.Response(status=200)


async def list_package_types(request: web.Request, ) -> web.Response:
    """List Custom Package Types

    List the custom package types associated with the account


    """
    return web.Response(status=200)


async def update_package_type(request: web.Request, package_id, body) -> web.Response:
    """Update Custom Package Type By ID

    Update the custom package type object by ID

    :param package_id: Package ID
    :type package_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePackageTypeRequestBody.from_dict(body)
    return web.Response(status=200)
