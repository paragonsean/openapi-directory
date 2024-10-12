from typing import List, Dict
from aiohttp import web

from openapi_server.models.dashboard import Dashboard
from openapi_server.models.dashboard_list_result import DashboardListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patchable_dashboard import PatchableDashboard
from openapi_server import util


async def dashboards_create_or_update(request: web.Request, subscription_id, resource_group_name, dashboard_name, api_version, dashboard) -> web.Response:
    """dashboards_create_or_update

    Creates or updates a Dashboard.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param dashboard_name: The name of the dashboard.
    :type dashboard_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param dashboard: The parameters required to create or update a dashboard.
    :type dashboard: dict | bytes

    """
    dashboard = Dashboard.from_dict(dashboard)
    return web.Response(status=200)


async def dashboards_delete(request: web.Request, subscription_id, resource_group_name, dashboard_name, api_version) -> web.Response:
    """dashboards_delete

    Deletes the Dashboard.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param dashboard_name: The name of the dashboard.
    :type dashboard_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def dashboards_get(request: web.Request, subscription_id, resource_group_name, dashboard_name, api_version) -> web.Response:
    """dashboards_get

    Gets the Dashboard.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param dashboard_name: The name of the dashboard.
    :type dashboard_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def dashboards_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """dashboards_list_by_resource_group

    Gets all the Dashboards within a resource group.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def dashboards_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """dashboards_list_by_subscription

    Gets all the dashboards within a subscription.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def dashboards_update(request: web.Request, subscription_id, resource_group_name, dashboard_name, api_version, dashboard) -> web.Response:
    """dashboards_update

    Updates an existing Dashboard.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param dashboard_name: The name of the dashboard.
    :type dashboard_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param dashboard: The updatable fields of a Dashboard.
    :type dashboard: dict | bytes

    """
    dashboard = PatchableDashboard.from_dict(dashboard)
    return web.Response(status=200)
