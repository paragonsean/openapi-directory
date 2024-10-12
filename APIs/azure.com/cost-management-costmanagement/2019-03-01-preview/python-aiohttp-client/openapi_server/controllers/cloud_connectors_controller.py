from typing import List, Dict
from aiohttp import web

from openapi_server.models.connector_definition import ConnectorDefinition
from openapi_server.models.connector_definition_list_result import ConnectorDefinitionListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def cloud_connector_create_or_update(request: web.Request, api_version, connector_name, connector) -> web.Response:
    """cloud_connector_create_or_update

    Create or update a cloud connector definition

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param connector_name: Connector Name.
    :type connector_name: str
    :param connector: Connector details
    :type connector: dict | bytes

    """
    connector = ConnectorDefinition.from_dict(connector)
    return web.Response(status=200)


async def cloud_connector_delete(request: web.Request, api_version, connector_name) -> web.Response:
    """cloud_connector_delete

    Delete a cloud connector definition

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param connector_name: Connector Name.
    :type connector_name: str

    """
    return web.Response(status=200)


async def cloud_connector_get(request: web.Request, api_version, connector_name, expand=None) -> web.Response:
    """cloud_connector_get

    Get a cloud connector definition

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param connector_name: Connector Name.
    :type connector_name: str
    :param expand: May be used to expand the collectionInfo property. By default, collectionInfo is not included.
    :type expand: str

    """
    return web.Response(status=200)


async def cloud_connector_list(request: web.Request, api_version) -> web.Response:
    """cloud_connector_list

    List all cloud connector definitions

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str

    """
    return web.Response(status=200)


async def cloud_connector_update(request: web.Request, api_version, connector_name, connector) -> web.Response:
    """cloud_connector_update

    Update a cloud connector definition

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param connector_name: Connector Name.
    :type connector_name: str
    :param connector: Connector details
    :type connector: dict | bytes

    """
    connector = ConnectorDefinition.from_dict(connector)
    return web.Response(status=200)
