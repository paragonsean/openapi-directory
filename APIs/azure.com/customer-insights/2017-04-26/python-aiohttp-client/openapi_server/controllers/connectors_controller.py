from typing import List, Dict
from aiohttp import web

from openapi_server.models.connector_list_result import ConnectorListResult
from openapi_server.models.connector_resource_format import ConnectorResourceFormat
from openapi_server import util


async def connectors_create_or_update(request: web.Request, resource_group_name, hub_name, connector_name, api_version, subscription_id, parameters) -> web.Response:
    """connectors_create_or_update

    Creates a connector or updates an existing connector in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param connector_name: The name of the connector.
    :type connector_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate Connector operation.
    :type parameters: dict | bytes

    """
    parameters = ConnectorResourceFormat.from_dict(parameters)
    return web.Response(status=200)


async def connectors_delete(request: web.Request, resource_group_name, hub_name, connector_name, api_version, subscription_id) -> web.Response:
    """connectors_delete

    Deletes a connector in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param connector_name: The name of the connector.
    :type connector_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def connectors_get(request: web.Request, resource_group_name, hub_name, connector_name, api_version, subscription_id) -> web.Response:
    """connectors_get

    Gets a connector in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param connector_name: The name of the connector.
    :type connector_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def connectors_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id) -> web.Response:
    """connectors_list_by_hub

    Gets all the connectors in the specified hub.

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
