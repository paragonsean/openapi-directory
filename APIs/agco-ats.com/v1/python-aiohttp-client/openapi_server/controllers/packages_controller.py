from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_package import APIPagedResponseUpdateSystemModelsPackage
from openapi_server.models.update_system_models_package import UpdateSystemModelsPackage
from openapi_server import util


async def packages_delete_package(request: web.Request, id) -> web.Response:
    """Delete a Package.

    No Documentation Found.

    :param id: The Package ID to Delete
    :type id: str

    """
    return web.Response(status=200)


async def packages_get_package(request: web.Request, id) -> web.Response:
    """Find a Package.

    No Documentation Found.

    :param id: The Package ID to Search for
    :type id: str

    """
    return web.Response(status=200)


async def packages_get_packages(request: web.Request, limit=None, offset=None, package_type_id=None, version=None, released=None) -> web.Response:
    """List Packages.

    No Documentation Found.

    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int
    :param package_type_id: Optional. If provided, filters by PackageTypeID.
    :type package_type_id: str
    :param version: Optional. If provided, filters by Version.
    :type version: int
    :param released: Optional. If provided, filters by Released.
    :type released: bool

    """
    return web.Response(status=200)


async def packages_post_package(request: web.Request, body) -> web.Response:
    """Add a Package to the Update System.

    No Documentation Found.

    :param body: The package to add.
    :type body: dict | bytes

    """
    body = UpdateSystemModelsPackage.from_dict(body)
    return web.Response(status=200)


async def packages_put_package(request: web.Request, id, body) -> web.Response:
    """Modify a Packge to the Update System.

    No Documentation Found.

    :param id: The unique ID of the Package
    :type id: str
    :param body: The package to update.
    :type body: dict | bytes

    """
    body = UpdateSystemModelsPackage.from_dict(body)
    return web.Response(status=200)
