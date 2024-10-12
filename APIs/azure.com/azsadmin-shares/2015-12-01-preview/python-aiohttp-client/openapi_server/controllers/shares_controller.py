from typing import List, Dict
from aiohttp import web

from openapi_server.models.share import Share
from openapi_server.models.shares_list_metric_definitions200_response import SharesListMetricDefinitions200Response
from openapi_server.models.shares_list_metrics200_response import SharesListMetrics200Response
from openapi_server import util


async def shares_get(request: web.Request, subscription_id, resource_group_name, farm_id, share_name, api_version) -> web.Response:
    """shares_get

    Returns a storage share.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param share_name: Share name.
    :type share_name: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def shares_list(request: web.Request, subscription_id, resource_group_name, farm_id, api_version) -> web.Response:
    """shares_list

    Returns a list of storage shares.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def shares_list_metric_definitions(request: web.Request, subscription_id, resource_group_name, farm_id, share_name, api_version) -> web.Response:
    """shares_list_metric_definitions

    Returns a list of metric definitions for a storage share.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param share_name: Share name.
    :type share_name: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def shares_list_metrics(request: web.Request, subscription_id, resource_group_name, farm_id, share_name, api_version) -> web.Response:
    """shares_list_metrics

    Returns a list of metrics for a storage share.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param share_name: Share name.
    :type share_name: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
