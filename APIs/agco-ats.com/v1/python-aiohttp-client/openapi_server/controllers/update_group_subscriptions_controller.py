from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_update_group_subscription import APIPagedResponseUpdateSystemModelsUpdateGroupSubscription
from openapi_server.models.update_system_models_update_group_subscription import UpdateSystemModelsUpdateGroupSubscription
from openapi_server import util


async def update_group_subscriptions_delete_update_group_subscription(request: web.Request, update_group_subscription_id) -> web.Response:
    """Delete an Update Group Subscription

    No Documentation Found.

    :param update_group_subscription_id: The Update Group Subscription ID to delete
    :type update_group_subscription_id: int

    """
    return web.Response(status=200)


async def update_group_subscriptions_get_update_group_subscription(request: web.Request, update_group_subscription_id) -> web.Response:
    """Get an Update Group Subscription

    No Documentation Found.

    :param update_group_subscription_id: The Update Group Subscription ID
    :type update_group_subscription_id: int

    """
    return web.Response(status=200)


async def update_group_subscriptions_get_update_group_subscriptions(request: web.Request, update_group_id=None, package_type_id=None, client_id=None, limit=None, offset=None) -> web.Response:
    """Get Update Group Subscriptions

    No Documentation Found.

    :param update_group_id: Optional. Filter by Update Group ID.
    :type update_group_id: str
    :param package_type_id: Optional. Filter by Package Type ID.
    :type package_type_id: str
    :param client_id: Optional. Filter by Client ID.
    :type client_id: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def update_group_subscriptions_post_update_group_subscription(request: web.Request, body) -> web.Response:
    """Add an Update Group Subscription

    No Documentation Found.

    :param body: The Update Group Subscription to add
    :type body: dict | bytes

    """
    body = UpdateSystemModelsUpdateGroupSubscription.from_dict(body)
    return web.Response(status=200)


async def update_group_subscriptions_post_update_group_subscriptions(request: web.Request, body) -> web.Response:
    """No Documentation Found.

    No Documentation Found.

    :param body: 
    :type body: list | bytes

    """
    body = [UpdateSystemModelsUpdateGroupSubscription.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_group_subscriptions_put_update_group_subscription(request: web.Request, update_group_subscription_id, body) -> web.Response:
    """Update an Update Group Subscription

    No Documentation Found.

    :param update_group_subscription_id: The Update Group Subscription ID
    :type update_group_subscription_id: int
    :param body: The updated Update Group Subscription
    :type body: dict | bytes

    """
    body = UpdateSystemModelsUpdateGroupSubscription.from_dict(body)
    return web.Response(status=200)


async def update_group_subscriptions_put_update_group_subscriptions(request: web.Request, body) -> web.Response:
    """No Documentation Found.

    No Documentation Found.

    :param body: 
    :type body: list | bytes

    """
    body = [UpdateSystemModelsUpdateGroupSubscription.from_dict(d) for d in body]
    return web.Response(status=200)
