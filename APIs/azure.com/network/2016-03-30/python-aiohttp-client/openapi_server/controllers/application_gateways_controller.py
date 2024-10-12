from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_gateway import ApplicationGateway
from openapi_server.models.application_gateway_list_result import ApplicationGatewayListResult
from openapi_server import util


async def application_gateways_create_or_update(request: web.Request, resource_group_name, application_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """application_gateways_create_or_update

    The Put ApplicationGateway operation creates/updates a ApplicationGateway

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_gateway_name: The name of the ApplicationGateway.
    :type application_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/delete ApplicationGateway operation
    :type parameters: dict | bytes

    """
    parameters = ApplicationGateway.from_dict(parameters)
    return web.Response(status=200)


async def application_gateways_delete(request: web.Request, resource_group_name, application_gateway_name, api_version, subscription_id) -> web.Response:
    """application_gateways_delete

    The delete application gateway operation deletes the specified application gateway.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_gateway_name: The name of the application gateway.
    :type application_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_gateways_get(request: web.Request, resource_group_name, application_gateway_name, api_version, subscription_id) -> web.Response:
    """application_gateways_get

    The Get application gateway operation retrieves information about the specified application gateway.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_gateway_name: The name of the application gateway.
    :type application_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_gateways_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """application_gateways_list

    The List ApplicationGateway operation retrieves all the application gateways in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_gateways_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """application_gateways_list_all

    The List application gateway operation retrieves all the application gateways in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_gateways_start(request: web.Request, resource_group_name, application_gateway_name, api_version, subscription_id) -> web.Response:
    """application_gateways_start

    The Start ApplicationGateway operation starts application gateway in the specified resource group through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_gateway_name: The name of the application gateway.
    :type application_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_gateways_stop(request: web.Request, resource_group_name, application_gateway_name, api_version, subscription_id) -> web.Response:
    """application_gateways_stop

    The STOP ApplicationGateway operation stops application gateway in the specified resource group through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_gateway_name: The name of the application gateway.
    :type application_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
