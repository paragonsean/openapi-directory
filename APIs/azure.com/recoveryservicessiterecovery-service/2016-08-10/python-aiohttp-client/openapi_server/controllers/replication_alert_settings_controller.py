from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert import Alert
from openapi_server.models.alert_collection import AlertCollection
from openapi_server.models.configure_alert_request import ConfigureAlertRequest
from openapi_server import util


async def replication_alert_settings_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, alert_setting_name, request) -> web.Response:
    """Configures email notifications for this vault.

    Create or update an email notification(alert) configuration.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param alert_setting_name: The name of the email notification(alert) configuration.
    :type alert_setting_name: str
    :param request: The input to configure the email notification(alert).
    :type request: dict | bytes

    """
    request = ConfigureAlertRequest.from_dict(request)
    return web.Response(status=200)


async def replication_alert_settings_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, alert_setting_name) -> web.Response:
    """Gets an email notification(alert) configuration.

    Gets the details of the specified email notification(alert) configuration.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param alert_setting_name: The name of the email notification configuration.
    :type alert_setting_name: str

    """
    return web.Response(status=200)


async def replication_alert_settings_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the list of configured email notification(alert) configurations.

    Gets the list of email notification(alert) configurations for the vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)
