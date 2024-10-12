from typing import List, Dict
from aiohttp import web

from openapi_server.models.connector_definition import ConnectorDefinition
from openapi_server.models.connector_definition_list_result import ConnectorDefinitionListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def connector_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, connector_name, connector) -> web.Response:
    """connector_create_or_update

    Create or update a connector definition

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param connector_name: Connector Name.
    :type connector_name: str
    :param connector: Connector details
    :type connector: dict | bytes

    """
    connector = ConnectorDefinition.from_dict(connector)
    return web.Response(status=200)


async def connector_delete(request: web.Request, api_version, subscription_id, resource_group_name, connector_name) -> web.Response:
    """connector_delete

    Delete a connector definition

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param connector_name: Connector Name.
    :type connector_name: str

    """
    return web.Response(status=200)


async def connector_get(request: web.Request, api_version, subscription_id, resource_group_name, connector_name) -> web.Response:
    """connector_get

    Get a connector definition

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param connector_name: Connector Name.
    :type connector_name: str

    """
    return web.Response(status=200)


async def connector_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """connector_list

    List all connector definitions for a subscription

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def connector_list_by_resource_group_name(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """connector_list_by_resource_group_name

    List all connector definitions for a resource group under a subscription.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def connector_update(request: web.Request, api_version, subscription_id, resource_group_name, connector_name, connector) -> web.Response:
    """connector_update

    Update a connector definition

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param connector_name: Connector Name.
    :type connector_name: str
    :param connector: Connector details
    :type connector: dict | bytes

    """
    connector = ConnectorDefinition.from_dict(connector)
    return web.Response(status=200)
