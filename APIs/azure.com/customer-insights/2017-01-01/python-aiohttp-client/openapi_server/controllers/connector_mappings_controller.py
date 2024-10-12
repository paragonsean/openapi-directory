from typing import List, Dict
from aiohttp import web

from openapi_server.models.connector_mapping_list_result import ConnectorMappingListResult
from openapi_server.models.connector_mapping_resource_format import ConnectorMappingResourceFormat
from openapi_server import util


async def connector_mappings_create_or_update(request: web.Request, resource_group_name, hub_name, connector_name, mapping_name, api_version, subscription_id, parameters) -> web.Response:
    """connector_mappings_create_or_update

    Creates a connector mapping or updates an existing connector mapping in the connector.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param connector_name: The name of the connector.
    :type connector_name: str
    :param mapping_name: The name of the connector mapping.
    :type mapping_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate Connector Mapping operation.
    :type parameters: dict | bytes

    """
    parameters = ConnectorMappingResourceFormat.from_dict(parameters)
    return web.Response(status=200)


async def connector_mappings_delete(request: web.Request, resource_group_name, hub_name, connector_name, mapping_name, api_version, subscription_id) -> web.Response:
    """connector_mappings_delete

    Deletes a connector mapping in the connector.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param connector_name: The name of the connector.
    :type connector_name: str
    :param mapping_name: The name of the connector mapping.
    :type mapping_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def connector_mappings_get(request: web.Request, resource_group_name, hub_name, connector_name, mapping_name, api_version, subscription_id) -> web.Response:
    """connector_mappings_get

    Gets a connector mapping in the connector.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param connector_name: The name of the connector.
    :type connector_name: str
    :param mapping_name: The name of the connector mapping.
    :type mapping_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def connector_mappings_list_by_connector(request: web.Request, resource_group_name, hub_name, connector_name, api_version, subscription_id) -> web.Response:
    """connector_mappings_list_by_connector

    Gets all the connector mappings in the specified connector.

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
