from typing import List, Dict
from aiohttp import web

from openapi_server.models.export_configurations_list200_response import ExportConfigurationsList200Response
from openapi_server.models.export_configurations_list200_response_values_inner import ExportConfigurationsList200ResponseValuesInner
from openapi_server.models.export_configurations_list200_response_values_inner_export_configuration import ExportConfigurationsList200ResponseValuesInnerExportConfiguration
from openapi_server.models.organizations_list_administered_default_response import OrganizationsListAdministeredDefaultResponse
from openapi_server import util


async def export_configurations_create(request: web.Request, owner_name, app_name, body) -> web.Response:
    """export_configurations_create

    Create new export configuration

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Export configurations.
    :type body: dict | bytes

    """
    body = ExportConfigurationsList200ResponseValuesInnerExportConfiguration.from_dict(body)
    return web.Response(status=200)


async def export_configurations_delete(request: web.Request, export_configuration_id, owner_name, app_name) -> web.Response:
    """export_configurations_delete

    Delete export configuration.

    :param export_configuration_id: The id of the export configuration.
    :type export_configuration_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def export_configurations_disable(request: web.Request, export_configuration_id, owner_name, app_name) -> web.Response:
    """export_configurations_disable

    Disable export configuration.

    :param export_configuration_id: The id of the export configuration.
    :type export_configuration_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def export_configurations_enable(request: web.Request, export_configuration_id, owner_name, app_name) -> web.Response:
    """export_configurations_enable

    Enable export configuration.

    :param export_configuration_id: The id of the export configuration.
    :type export_configuration_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def export_configurations_get(request: web.Request, export_configuration_id, owner_name, app_name) -> web.Response:
    """export_configurations_get

    Get export configuration.

    :param export_configuration_id: The id of the export configuration.
    :type export_configuration_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def export_configurations_list(request: web.Request, owner_name, app_name) -> web.Response:
    """export_configurations_list

    List export configurations.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def export_configurations_partial_update(request: web.Request, export_configuration_id, owner_name, app_name, body) -> web.Response:
    """export_configurations_partial_update

    Partially update export configuration.

    :param export_configuration_id: The id of the export configuration.
    :type export_configuration_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Export configurations.
    :type body: dict | bytes

    """
    body = ExportConfigurationsList200ResponseValuesInnerExportConfiguration.from_dict(body)
    return web.Response(status=200)
