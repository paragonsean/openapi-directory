from typing import List, Dict
from aiohttp import web

from openapi_server.models.server_security_alert_policy import ServerSecurityAlertPolicy
from openapi_server import util


async def server_security_alert_policies_create_or_update(request: web.Request, resource_group_name, server_name, security_alert_policy_name, subscription_id, api_version, parameters) -> web.Response:
    """server_security_alert_policies_create_or_update

    Creates or updates a threat detection policy.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param security_alert_policy_name: The name of the threat detection policy.
    :type security_alert_policy_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The server security alert policy.
    :type parameters: dict | bytes

    """
    parameters = ServerSecurityAlertPolicy.from_dict(parameters)
    return web.Response(status=200)


async def server_security_alert_policies_get(request: web.Request, resource_group_name, server_name, security_alert_policy_name, subscription_id, api_version) -> web.Response:
    """server_security_alert_policies_get

    Get a server&#39;s security alert policy.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param security_alert_policy_name: The name of the security alert policy.
    :type security_alert_policy_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
