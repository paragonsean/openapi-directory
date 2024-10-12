from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.service_diagnostic_settings_resource import ServiceDiagnosticSettingsResource
from openapi_server.models.service_diagnostic_settings_resource_patch import ServiceDiagnosticSettingsResourcePatch
from openapi_server import util


async def service_diagnostic_settings_update(request: web.Request, resource_uri, api_version, service_diagnostic_settings_resource) -> web.Response:
    """service_diagnostic_settings_update

    Updates an existing ServiceDiagnosticSettingsResource. To update other fields use the CreateOrUpdate method. **WARNING**: This method will be deprecated in future releases.

    :param resource_uri: The identifier of the resource.
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param service_diagnostic_settings_resource: Parameters supplied to the operation.
    :type service_diagnostic_settings_resource: dict | bytes

    """
    service_diagnostic_settings_resource = ServiceDiagnosticSettingsResourcePatch.from_dict(service_diagnostic_settings_resource)
    return web.Response(status=200)
