from typing import List, Dict
from aiohttp import web

from openapi_server.models.export_request import ExportRequest
from openapi_server.models.import_export_response import ImportExportResponse
from openapi_server.models.import_extension_request import ImportExtensionRequest
from openapi_server.models.import_request import ImportRequest
from openapi_server import util


async def databases_create_import_operation(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, extension_name, parameters) -> web.Response:
    """databases_create_import_operation

    Creates an import operation that imports a bacpac into an existing database. The existing database must be empty.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database to import into
    :type database_name: str
    :param extension_name: The name of the operation to perform
    :type extension_name: str
    :param parameters: The required parameters for importing a Bacpac into a database.
    :type parameters: dict | bytes

    """
    parameters = ImportExtensionRequest.from_dict(parameters)
    return web.Response(status=200)


async def databases_export(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, parameters) -> web.Response:
    """databases_export

    Exports a database to a bacpac.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database to be exported.
    :type database_name: str
    :param parameters: The required parameters for exporting a database.
    :type parameters: dict | bytes

    """
    parameters = ExportRequest.from_dict(parameters)
    return web.Response(status=200)


async def databases_import(request: web.Request, api_version, subscription_id, resource_group_name, server_name, parameters) -> web.Response:
    """databases_import

    Imports a bacpac into a new database. 

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param parameters: The required parameters for importing a Bacpac into a database.
    :type parameters: dict | bytes

    """
    parameters = ImportRequest.from_dict(parameters)
    return web.Response(status=200)
