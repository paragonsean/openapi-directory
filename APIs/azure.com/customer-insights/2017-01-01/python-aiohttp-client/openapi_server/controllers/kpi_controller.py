from typing import List, Dict
from aiohttp import web

from openapi_server.models.kpi_list_result import KpiListResult
from openapi_server.models.kpi_resource_format import KpiResourceFormat
from openapi_server import util


async def kpi_create_or_update(request: web.Request, resource_group_name, hub_name, kpi_name, api_version, subscription_id, parameters) -> web.Response:
    """kpi_create_or_update

    Creates a KPI or updates an existing KPI in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param kpi_name: The name of the KPI.
    :type kpi_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/update KPI operation.
    :type parameters: dict | bytes

    """
    parameters = KpiResourceFormat.from_dict(parameters)
    return web.Response(status=200)


async def kpi_delete(request: web.Request, resource_group_name, hub_name, kpi_name, api_version, subscription_id) -> web.Response:
    """kpi_delete

    Deletes a KPI in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param kpi_name: The name of the KPI.
    :type kpi_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def kpi_get(request: web.Request, resource_group_name, hub_name, kpi_name, api_version, subscription_id) -> web.Response:
    """kpi_get

    Gets a KPI in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param kpi_name: The name of the KPI.
    :type kpi_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def kpi_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id) -> web.Response:
    """kpi_list_by_hub

    Gets all the KPIs in the specified hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def kpi_reprocess(request: web.Request, resource_group_name, hub_name, kpi_name, api_version, subscription_id) -> web.Response:
    """kpi_reprocess

    Reprocesses the Kpi values of the specified KPI.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param kpi_name: The name of the KPI.
    :type kpi_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
