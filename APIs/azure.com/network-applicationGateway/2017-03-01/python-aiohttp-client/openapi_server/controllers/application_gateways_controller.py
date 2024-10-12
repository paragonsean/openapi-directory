from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_gateway import ApplicationGateway
from openapi_server.models.application_gateway_available_waf_rule_sets_result import ApplicationGatewayAvailableWafRuleSetsResult
from openapi_server.models.application_gateway_backend_health import ApplicationGatewayBackendHealth
from openapi_server.models.application_gateway_list_result import ApplicationGatewayListResult
from openapi_server import util


async def application_gateways_backend_health(request: web.Request, resource_group_name, application_gateway_name, api_version, subscription_id, expand=None) -> web.Response:
    """application_gateways_backend_health

    Gets the backend health of the specified application gateway in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_gateway_name: The name of the application gateway.
    :type application_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands BackendAddressPool and BackendHttpSettings referenced in backend health.
    :type expand: str

    """
    return web.Response(status=200)


async def application_gateways_create_or_update(request: web.Request, resource_group_name, application_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """application_gateways_create_or_update

    Creates or updates the specified application gateway.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_gateway_name: The name of the application gateway.
    :type application_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update application gateway operation.
    :type parameters: dict | bytes

    """
    parameters = ApplicationGateway.from_dict(parameters)
    return web.Response(status=200)


async def application_gateways_delete(request: web.Request, resource_group_name, application_gateway_name, api_version, subscription_id) -> web.Response:
    """application_gateways_delete

    Deletes the specified application gateway.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_gateway_name: The name of the application gateway.
    :type application_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_gateways_get(request: web.Request, resource_group_name, application_gateway_name, api_version, subscription_id) -> web.Response:
    """application_gateways_get

    Gets the specified application gateway.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_gateway_name: The name of the application gateway.
    :type application_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_gateways_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """application_gateways_list

    Lists all application gateways in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_gateways_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """application_gateways_list_all

    Gets all the application gateways in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_gateways_list_available_waf_rule_sets(request: web.Request, api_version, subscription_id) -> web.Response:
    """application_gateways_list_available_waf_rule_sets

    Lists all available web application firewall rule sets.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_gateways_start(request: web.Request, resource_group_name, application_gateway_name, api_version, subscription_id) -> web.Response:
    """application_gateways_start

    Starts the specified application gateway.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_gateway_name: The name of the application gateway.
    :type application_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_gateways_stop(request: web.Request, resource_group_name, application_gateway_name, api_version, subscription_id) -> web.Response:
    """application_gateways_stop

    Stops the specified application gateway in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_gateway_name: The name of the application gateway.
    :type application_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
