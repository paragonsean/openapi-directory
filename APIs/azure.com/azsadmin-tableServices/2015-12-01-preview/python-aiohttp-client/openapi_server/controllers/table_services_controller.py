from typing import List, Dict
from aiohttp import web

from openapi_server.models.table_service import TableService
from openapi_server.models.table_services_list_metric_definitions200_response import TableServicesListMetricDefinitions200Response
from openapi_server.models.table_services_list_metrics200_response import TableServicesListMetrics200Response
from openapi_server import util


async def table_services_get(request: web.Request, subscription_id, resource_group_name, farm_id, service_type, api_version) -> web.Response:
    """table_services_get

    Returns the table service.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param service_type: The service type.
    :type service_type: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def table_services_list_metric_definitions(request: web.Request, subscription_id, resource_group_name, farm_id, service_type, api_version) -> web.Response:
    """table_services_list_metric_definitions

    Returns a list of metric definitions for table service.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param service_type: The service type.
    :type service_type: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def table_services_list_metrics(request: web.Request, subscription_id, resource_group_name, farm_id, service_type, api_version) -> web.Response:
    """table_services_list_metrics

    Returns a list of metrics for table service.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param service_type: The service type.
    :type service_type: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
