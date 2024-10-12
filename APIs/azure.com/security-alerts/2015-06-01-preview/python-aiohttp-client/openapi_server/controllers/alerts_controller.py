from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert import Alert
from openapi_server.models.alert_list import AlertList
from openapi_server.models.alerts_list_default_response import AlertsListDefaultResponse
from openapi_server import util


async def alerts_get_resource_group_level_alerts(request: web.Request, api_version, subscription_id, asc_location, alert_name, resource_group_name) -> web.Response:
    """alerts_get_resource_group_level_alerts

    Get an alert that is associated a resource group or a resource in a resource group

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param alert_name: Name of the alert object
    :type alert_name: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def alerts_get_subscription_level_alert(request: web.Request, api_version, subscription_id, asc_location, alert_name) -> web.Response:
    """alerts_get_subscription_level_alert

    Get an alert that is associated with a subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param alert_name: Name of the alert object
    :type alert_name: str

    """
    return web.Response(status=200)


async def alerts_list(request: web.Request, api_version, subscription_id, filter=None, select=None, expand=None) -> web.Response:
    """alerts_list

    List all the alerts that are associated with the subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param select: OData select. Optional.
    :type select: str
    :param expand: OData expand. Optional.
    :type expand: str

    """
    return web.Response(status=200)


async def alerts_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name, filter=None, select=None, expand=None) -> web.Response:
    """alerts_list_by_resource_group

    List all the alerts that are associated with the resource group

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param select: OData select. Optional.
    :type select: str
    :param expand: OData expand. Optional.
    :type expand: str

    """
    return web.Response(status=200)


async def alerts_list_resource_group_level_alerts_by_region(request: web.Request, api_version, subscription_id, asc_location, resource_group_name, filter=None, select=None, expand=None) -> web.Response:
    """alerts_list_resource_group_level_alerts_by_region

    List all the alerts that are associated with the resource group that are stored in a specific location

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param select: OData select. Optional.
    :type select: str
    :param expand: OData expand. Optional.
    :type expand: str

    """
    return web.Response(status=200)


async def alerts_list_subscription_level_alerts_by_region(request: web.Request, api_version, subscription_id, asc_location, filter=None, select=None, expand=None) -> web.Response:
    """alerts_list_subscription_level_alerts_by_region

    List all the alerts that are associated with the subscription that are stored in a specific location

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param select: OData select. Optional.
    :type select: str
    :param expand: OData expand. Optional.
    :type expand: str

    """
    return web.Response(status=200)


async def alerts_update_resource_group_level_alert_state_to_dismiss(request: web.Request, api_version, subscription_id, asc_location, alert_name, resource_group_name) -> web.Response:
    """alerts_update_resource_group_level_alert_state_to_dismiss

    Update the alert&#39;s state

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param alert_name: Name of the alert object
    :type alert_name: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def alerts_update_resource_group_level_alert_state_to_reactivate(request: web.Request, api_version, subscription_id, asc_location, alert_name, resource_group_name) -> web.Response:
    """alerts_update_resource_group_level_alert_state_to_reactivate

    Update the alert&#39;s state

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param alert_name: Name of the alert object
    :type alert_name: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def alerts_update_subscription_level_alert_state_to_dismiss(request: web.Request, api_version, subscription_id, asc_location, alert_name) -> web.Response:
    """alerts_update_subscription_level_alert_state_to_dismiss

    Update the alert&#39;s state

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param alert_name: Name of the alert object
    :type alert_name: str

    """
    return web.Response(status=200)


async def alerts_update_subscription_level_alert_state_to_reactivate(request: web.Request, api_version, subscription_id, asc_location, alert_name) -> web.Response:
    """alerts_update_subscription_level_alert_state_to_reactivate

    Update the alert&#39;s state

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param alert_name: Name of the alert object
    :type alert_name: str

    """
    return web.Response(status=200)
