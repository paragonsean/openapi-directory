from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.delete_operation_result import DeleteOperationResult
from openapi_server.models.traffic_manager_user_metrics_key_model import TrafficManagerUserMetricsKeyModel
from openapi_server import util


async def traffic_manager_user_metrics_keys_create_or_update(request: web.Request, api_version, subscription_id) -> web.Response:
    """traffic_manager_user_metrics_keys_create_or_update

    Create or update a subscription-level key used for Real User Metrics collection.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def traffic_manager_user_metrics_keys_delete(request: web.Request, api_version, subscription_id) -> web.Response:
    """traffic_manager_user_metrics_keys_delete

    Delete a subscription-level key used for Real User Metrics collection.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def traffic_manager_user_metrics_keys_get(request: web.Request, api_version, subscription_id) -> web.Response:
    """traffic_manager_user_metrics_keys_get

    Get the subscription-level key used for Real User Metrics collection.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
