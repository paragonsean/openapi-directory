from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_available_update_group_subscription import APIPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription
from openapi_server.models.api_paged_response_update_system_models_client import APIPagedResponseUpdateSystemModelsClient
from openapi_server.models.api_paged_response_update_system_models_update_group_subscription import APIPagedResponseUpdateSystemModelsUpdateGroupSubscription
from openapi_server.models.update_system_models_client import UpdateSystemModelsClient
from openapi_server import util


async def api_v2_clients_idget(request: web.Request, id) -> web.Response:
    """Get a Client in the Update System.

    No Documentation Found.

    :param id: The Client ID
    :type id: str

    """
    return web.Response(status=200)


async def clients_get(request: web.Request, tag=None, limit=None, offset=None) -> web.Response:
    """Get a List of Clients in the Update System.

    No Documentation Found.

    :param tag: Optional. Filter clients by Tag. Wildcards are supported (*).
    :type tag: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def clients_get_available_subscriptions(request: web.Request, id, update_group_id=None, limit=None, offset=None) -> web.Response:
    """Get a Client&#39;s Available Update Group Subscriptions

    No Documentation Found.

    :param id: The Client ID
    :type id: str
    :param update_group_id: Optional. Filter by Update Group.
    :type update_group_id: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def clients_get_subscriptions(request: web.Request, id, update_group_id=None, limit=None, offset=None) -> web.Response:
    """Get a Client&#39;s Current Update Group Subscriptions

    No Documentation Found.

    :param id: The Client ID
    :type id: str
    :param update_group_id: Optional. Filter by Update Group.
    :type update_group_id: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def clients_put(request: web.Request, id, body) -> web.Response:
    """Update a Client.

    No Documentation Found.

    :param id: The Client ID
    :type id: str
    :param body: Updated Client Object.
    :type body: dict | bytes

    """
    body = UpdateSystemModelsClient.from_dict(body)
    return web.Response(status=200)
