from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.guest_diagnostic_settings_association_list import GuestDiagnosticSettingsAssociationList
from openapi_server.models.guest_diagnostic_settings_association_resource import GuestDiagnosticSettingsAssociationResource
from openapi_server.models.guest_diagnostic_settings_association_resource_patch import GuestDiagnosticSettingsAssociationResourcePatch
from openapi_server import util


async def guest_diagnostics_settings_association_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """guest_diagnostics_settings_association_list

    Get a list of all guest diagnostic settings association in a subscription.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def guest_diagnostics_settings_association_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """guest_diagnostics_settings_association_list_by_resource_group

    Get a list of all guest diagnostic settings association in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def guest_diagnostics_settings_association_update(request: web.Request, resource_uri, api_version, association_name, parameters) -> web.Response:
    """guest_diagnostics_settings_association_update

    Updates an existing guestDiagnosticsSettingsAssociation Resource. To update other fields use the CreateOrUpdate method

    :param resource_uri: The fully qualified ID of the resource, including the resource name and resource type.
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param association_name: The name of the diagnostic settings association.
    :type association_name: str
    :param parameters: Parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = GuestDiagnosticSettingsAssociationResourcePatch.from_dict(parameters)
    return web.Response(status=200)
