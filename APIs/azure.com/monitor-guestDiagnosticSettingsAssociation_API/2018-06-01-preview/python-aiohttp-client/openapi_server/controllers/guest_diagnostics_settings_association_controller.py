from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.guest_diagnostic_settings_association_resource import GuestDiagnosticSettingsAssociationResource
from openapi_server import util


async def guest_diagnostics_settings_association_create_or_update(request: web.Request, resource_uri, association_name, api_version, diagnostic_settings_association) -> web.Response:
    """guest_diagnostics_settings_association_create_or_update

    Creates or updates guest diagnostics settings association.

    :param resource_uri: The fully qualified ID of the resource, including the resource name and resource type.
    :type resource_uri: str
    :param association_name: The name of the diagnostic settings association.
    :type association_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param diagnostic_settings_association: The diagnostic settings association to create or update.
    :type diagnostic_settings_association: dict | bytes

    """
    diagnostic_settings_association = GuestDiagnosticSettingsAssociationResource.from_dict(diagnostic_settings_association)
    return web.Response(status=200)


async def guest_diagnostics_settings_association_delete(request: web.Request, resource_uri, association_name, api_version) -> web.Response:
    """guest_diagnostics_settings_association_delete

    Delete guest diagnostics association settings.

    :param resource_uri: The fully qualified ID of the resource, including the resource name and resource type.
    :type resource_uri: str
    :param association_name: The name of the diagnostic settings association.
    :type association_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def guest_diagnostics_settings_association_get(request: web.Request, resource_uri, association_name, api_version) -> web.Response:
    """guest_diagnostics_settings_association_get

    Gets guest diagnostics association settings.

    :param resource_uri: The fully qualified ID of the resource, including the resource name and resource type.
    :type resource_uri: str
    :param association_name: The name of the diagnostic settings association.
    :type association_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
