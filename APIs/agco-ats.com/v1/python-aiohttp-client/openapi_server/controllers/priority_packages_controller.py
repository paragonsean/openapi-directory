from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_priority_package import APIPagedResponseUpdateSystemModelsPriorityPackage
from openapi_server.models.update_system_models_priority_package import UpdateSystemModelsPriorityPackage
from openapi_server import util


async def priority_packages_delete_priority_packages(request: web.Request, id) -> web.Response:
    """Delete a Priority Package for a Client.

    No Documentation Found.

    :param id: The Priority Package ID
    :type id: str

    """
    return web.Response(status=200)


async def priority_packages_get_priority_package(request: web.Request, id) -> web.Response:
    """Get a Priority Packages for a Client.

    No Documentation Found.

    :param id: The Priority Package ID
    :type id: str

    """
    return web.Response(status=200)


async def priority_packages_get_priority_packages(request: web.Request, client_id=None, status=None, limit=None, offset=None) -> web.Response:
    """Get a list of Priority Packages by Client.

    No Documentation Found.

    :param client_id: Optional. Filter priority packages by ClientID.
    :type client_id: str
    :param status: Optional. Filter returned packages by status. By default only active packages will be returned.
    :type status: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def priority_packages_post_priority_packages(request: web.Request, body) -> web.Response:
    """Add a Priority Package for a Client.

    No Documentation Found.

    :param body: The PriorityPackage to add
    :type body: dict | bytes

    """
    body = UpdateSystemModelsPriorityPackage.from_dict(body)
    return web.Response(status=200)
