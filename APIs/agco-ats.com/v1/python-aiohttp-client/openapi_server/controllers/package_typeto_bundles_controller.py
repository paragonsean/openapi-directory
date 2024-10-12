from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_package_type_i_dto_bundle import APIPagedResponseUpdateSystemModelsPackageTypeIDtoBundle
from openapi_server.models.update_system_models_package_type_i_dto_bundle import UpdateSystemModelsPackageTypeIDtoBundle
from openapi_server import util


async def package_typeto_bundles_delete(request: web.Request, bundle_id, package_type_id) -> web.Response:
    """Delete a Package Type to Bundle Relationship.

    No Documentation Found.

    :param bundle_id: The BundleID
    :type bundle_id: str
    :param package_type_id: The PackageTypeID
    :type package_type_id: str

    """
    return web.Response(status=200)


async def package_typeto_bundles_get(request: web.Request, bundle_id=None, limit=None, offset=None) -> web.Response:
    """Get all of the Package Type to Bundle Relationships.

    No Documentation Found.

    :param bundle_id: Optional. Filter by BundleID.
    :type bundle_id: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def package_typeto_bundles_post(request: web.Request, body) -> web.Response:
    """Add a new Package Type ID to Bundle Relationship.

    No Documentation Found.

    :param body: The PackageTypeToBundle to add.
    :type body: dict | bytes

    """
    body = UpdateSystemModelsPackageTypeIDtoBundle.from_dict(body)
    return web.Response(status=200)


async def package_typeto_bundles_put(request: web.Request, body) -> web.Response:
    """Update a Package Type ID to Bundle Relationship.

    No Documentation Found.

    :param body: The PackageTypeToBundle to update.
    :type body: dict | bytes

    """
    body = UpdateSystemModelsPackageTypeIDtoBundle.from_dict(body)
    return web.Response(status=200)
