from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_bundle import APIPagedResponseUpdateSystemModelsBundle
from openapi_server.models.update_system_models_bundle import UpdateSystemModelsBundle
from openapi_server import util


async def bundles_delete_bundle(request: web.Request, id) -> web.Response:
    """Delete a Bundle.

    No Documentation Found.

    :param id: The Bundle ID to Delete
    :type id: str

    """
    return web.Response(status=200)


async def bundles_get_bundle(request: web.Request, id) -> web.Response:
    """Get a specific Bundle by ID.

    No Documentation Found.

    :param id: The Bundle ID
    :type id: str

    """
    return web.Response(status=200)


async def bundles_get_bundles(request: web.Request, update_group_id=None, active=None, limit=None, offset=None, bundle_number=None) -> web.Response:
    """Get the list of bundles.

    No Documentation Found.

    :param update_group_id: Optional. Filter by UpdateGroup ID.
    :type update_group_id: str
    :param active: Optional. Filter by active status.
    :type active: bool
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int
    :param bundle_number: Optional. If provided, filters by BundleNumber.
    :type bundle_number: int

    """
    return web.Response(status=200)


async def bundles_post_bundle(request: web.Request, body) -> web.Response:
    """Add a Bundle to the Update System.

    No Documentation Found.

    :param body: The bundle to add
    :type body: dict | bytes

    """
    body = UpdateSystemModelsBundle.from_dict(body)
    return web.Response(status=200)


async def bundles_put_bundle(request: web.Request, id, body) -> web.Response:
    """Modify a Bundle in the Update System.

    No Documentation Found.

    :param id: The unique ID of the Bundle
    :type id: str
    :param body: The bundle to modify
    :type body: dict | bytes

    """
    body = UpdateSystemModelsBundle.from_dict(body)
    return web.Response(status=200)
