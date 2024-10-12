from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_package_type import APIPagedResponseUpdateSystemModelsPackageType
from openapi_server.models.update_system_models_package_type import UpdateSystemModelsPackageType
from openapi_server import util


async def api_v2_package_types_idget(request: web.Request, id) -> web.Response:
    """Get a specific Package Type.

    No Documentation Found.

    :param id: The Package Type ID
    :type id: str

    """
    return web.Response(status=200)


async def package_types_add_package_type_user(request: web.Request, id, user_id) -> web.Response:
    """Add a package type that a user can see.

    No Documentation Found.

    :param id: The ID of the Package Type
    :type id: str
    :param user_id: The userID to link to the package type
    :type user_id: int

    """
    return web.Response(status=200)


async def package_types_delete(request: web.Request, id) -> web.Response:
    """Delete a Package Type.

    No Documentation Found.

    :param id: The Package Type ID
    :type id: str

    """
    return web.Response(status=200)


async def package_types_get(request: web.Request, limit=None, offset=None, user_id=None) -> web.Response:
    """Get all of the Package Types.

    No Documentation Found.

    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int
    :param user_id: Optional. The user ID to sort packageTypes by the user&#39;s access
    :type user_id: int

    """
    return web.Response(status=200)


async def package_types_post(request: web.Request, body) -> web.Response:
    """Add a Package Type.

    No Documentation Found.

    :param body: The Package Type to add
    :type body: dict | bytes

    """
    body = UpdateSystemModelsPackageType.from_dict(body)
    return web.Response(status=200)


async def package_types_put(request: web.Request, id, body) -> web.Response:
    """Modify a Package Type.

    No Documentation Found.

    :param id: The ID of the Package Type
    :type id: str
    :param body: The Package Type to update
    :type body: dict | bytes

    """
    body = UpdateSystemModelsPackageType.from_dict(body)
    return web.Response(status=200)


async def package_types_remove_package_type_user(request: web.Request, id, user_id) -> web.Response:
    """Deletes a package type a user could see.

    No Documentation Found.

    :param id: The ID of the Package Type
    :type id: str
    :param user_id: The userID to link to the package type
    :type user_id: int

    """
    return web.Response(status=200)
