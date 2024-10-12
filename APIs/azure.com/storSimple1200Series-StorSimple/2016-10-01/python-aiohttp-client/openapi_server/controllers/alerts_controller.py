from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert_list import AlertList
from openapi_server.models.clear_alert_request import ClearAlertRequest
from openapi_server.models.error import Error
from openapi_server.models.send_test_alert_email_request import SendTestAlertEmailRequest
from openapi_server import util


async def alerts_clear(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, request) -> web.Response:
    """alerts_clear

    Clear the alerts.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param request: The clear alert request.
    :type request: dict | bytes

    """
    request = ClearAlertRequest.from_dict(request)
    return web.Response(status=200)


async def alerts_list_by_manager(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, filter=None) -> web.Response:
    """alerts_list_by_manager

    Retrieves all the alerts in a manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)


async def alerts_send_test_email(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, request) -> web.Response:
    """alerts_send_test_email

    Sends a test alert email.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param request: The send test alert email request.
    :type request: dict | bytes

    """
    request = SendTestAlertEmailRequest.from_dict(request)
    return web.Response(status=200)
