from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_bundle import APIPagedResponseUpdateSystemModelsBundle
from openapi_server.models.api_paged_response_update_system_models_update_group import APIPagedResponseUpdateSystemModelsUpdateGroup
from openapi_server.models.update_system_models_update_group import UpdateSystemModelsUpdateGroup
from openapi_server import util


async def api_v2_update_groups_idget(request: web.Request, id) -> web.Response:
    """Get a specific Update Group by ID.

    No Documentation Found.

    :param id: The ID of the Update Group
    :type id: str

    """
    return web.Response(status=200)


async def update_groups_add_update_group_user(request: web.Request, id, user_id) -> web.Response:
    """Add an updateGroup that a user can see.

    No Documentation Found.

    :param id: The ID of the update group
    :type id: str
    :param user_id: The userID to link to the update group
    :type user_id: int

    """
    return web.Response(status=200)


async def update_groups_delete(request: web.Request, id) -> web.Response:
    """Delete an Update Group.

    No Documentation Found.

    :param id: The ID of the Update Group to Delete
    :type id: str

    """
    return web.Response(status=200)


async def update_groups_get(request: web.Request, limit=None, offset=None, user_id=None) -> web.Response:
    """Get a list of Update Groups.  Update Groups are used by the client to register for a specific type of update.

    No Documentation Found.

    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int
    :param user_id: Optional. The user ID to sort update groups by the user&#39;s access
    :type user_id: int

    """
    return web.Response(status=200)


async def update_groups_get_update_group_bundles(request: web.Request, id, include_inactive, limit=None, offset=None) -> web.Response:
    """Get a list of bundles for UpdateGroup.

    No Documentation Found.

    :param id: The UpdateGroupID
    :type id: str
    :param include_inactive: Include Inactive Bundles (true|false)
    :type include_inactive: bool
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def update_groups_post(request: web.Request, body) -> web.Response:
    """Add a new Update Group.  The report field is a string that has a dot based request for a specific piece of submitted data.

    No Documentation Found.

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateSystemModelsUpdateGroup.from_dict(body)
    return web.Response(status=200)


async def update_groups_put(request: web.Request, id, body) -> web.Response:
    """Modify an Update Group.

    No Documentation Found.

    :param id: ID of the Update Group
    :type id: str
    :param body: The Update Group to update.
    :type body: dict | bytes

    """
    body = UpdateSystemModelsUpdateGroup.from_dict(body)
    return web.Response(status=200)


async def update_groups_remove_update_group_user(request: web.Request, id, user_id) -> web.Response:
    """Deletes an update group a user could see.

    No Documentation Found.

    :param id: The ID of the update group
    :type id: str
    :param user_id: The userID to link to the update group
    :type user_id: int

    """
    return web.Response(status=200)
