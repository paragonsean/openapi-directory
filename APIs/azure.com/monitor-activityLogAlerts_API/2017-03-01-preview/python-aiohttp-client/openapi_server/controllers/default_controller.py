from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_log_alert_list import ActivityLogAlertList
from openapi_server.models.activity_log_alert_resource import ActivityLogAlertResource
from openapi_server.models.activity_log_alert_resource_patch import ActivityLogAlertResourcePatch
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def activity_log_alerts_create_or_update(request: web.Request, subscription_id, resource_group_name, activity_log_alert_name, api_version, activity_log_alert) -> web.Response:
    """activity_log_alerts_create_or_update

    Create a new activity log alert or update an existing one.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param activity_log_alert_name: The name of the activity log alert.
    :type activity_log_alert_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param activity_log_alert: The activity log alert to create or use for the update.
    :type activity_log_alert: dict | bytes

    """
    activity_log_alert = ActivityLogAlertResource.from_dict(activity_log_alert)
    return web.Response(status=200)


async def activity_log_alerts_delete(request: web.Request, subscription_id, resource_group_name, activity_log_alert_name, api_version) -> web.Response:
    """activity_log_alerts_delete

    Delete an activity log alert.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param activity_log_alert_name: The name of the activity log alert.
    :type activity_log_alert_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def activity_log_alerts_get(request: web.Request, subscription_id, resource_group_name, activity_log_alert_name, api_version) -> web.Response:
    """activity_log_alerts_get

    Get an activity log alert.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param activity_log_alert_name: The name of the activity log alert.
    :type activity_log_alert_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def activity_log_alerts_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """activity_log_alerts_list_by_resource_group

    Get a list of all activity log alerts in a resource group.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def activity_log_alerts_list_by_subscription_id(request: web.Request, subscription_id, api_version) -> web.Response:
    """activity_log_alerts_list_by_subscription_id

    Get a list of all activity log alerts in a subscription.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def activity_log_alerts_update(request: web.Request, subscription_id, resource_group_name, activity_log_alert_name, api_version, activity_log_alert_patch) -> web.Response:
    """activity_log_alerts_update

    Updates an existing ActivityLogAlertResource&#39;s tags. To update other fields use the CreateOrUpdate method.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param activity_log_alert_name: The name of the activity log alert.
    :type activity_log_alert_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param activity_log_alert_patch: Parameters supplied to the operation.
    :type activity_log_alert_patch: dict | bytes

    """
    activity_log_alert_patch = ActivityLogAlertResourcePatch.from_dict(activity_log_alert_patch)
    return web.Response(status=200)
