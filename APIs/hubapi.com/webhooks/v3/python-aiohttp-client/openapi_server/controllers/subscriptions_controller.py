from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_input_subscription_batch_update_request import BatchInputSubscriptionBatchUpdateRequest
from openapi_server.models.batch_response_subscription_response import BatchResponseSubscriptionResponse
from openapi_server.models.batch_response_subscription_response_with_errors import BatchResponseSubscriptionResponseWithErrors
from openapi_server.models.error import Error
from openapi_server.models.subscription_create_request import SubscriptionCreateRequest
from openapi_server.models.subscription_list_response import SubscriptionListResponse
from openapi_server.models.subscription_patch_request import SubscriptionPatchRequest
from openapi_server.models.subscription_response import SubscriptionResponse
from openapi_server import util


async def delete_webhooks_v3_app_id_subscriptions_subscription_id_archive(request: web.Request, subscription_id, app_id) -> web.Response:
    """delete_webhooks_v3_app_id_subscriptions_subscription_id_archive

    

    :param subscription_id: 
    :type subscription_id: int
    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)


async def get_webhooks_v3_app_id_subscriptions_get_all(request: web.Request, app_id) -> web.Response:
    """get_webhooks_v3_app_id_subscriptions_get_all

    

    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)


async def get_webhooks_v3_app_id_subscriptions_subscription_id_get_by_id(request: web.Request, subscription_id, app_id) -> web.Response:
    """get_webhooks_v3_app_id_subscriptions_subscription_id_get_by_id

    

    :param subscription_id: 
    :type subscription_id: int
    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)


async def patch_webhooks_v3_app_id_subscriptions_subscription_id_update(request: web.Request, subscription_id, app_id, body) -> web.Response:
    """patch_webhooks_v3_app_id_subscriptions_subscription_id_update

    

    :param subscription_id: 
    :type subscription_id: int
    :param app_id: 
    :type app_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionPatchRequest.from_dict(body)
    return web.Response(status=200)


async def post_webhooks_v3_app_id_subscriptions_batch_update_update_batch(request: web.Request, app_id, body) -> web.Response:
    """post_webhooks_v3_app_id_subscriptions_batch_update_update_batch

    

    :param app_id: 
    :type app_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = BatchInputSubscriptionBatchUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def post_webhooks_v3_app_id_subscriptions_create(request: web.Request, app_id, body) -> web.Response:
    """post_webhooks_v3_app_id_subscriptions_create

    

    :param app_id: 
    :type app_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionCreateRequest.from_dict(body)
    return web.Response(status=200)
