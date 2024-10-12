from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.service_diagnostic_settings_resource import ServiceDiagnosticSettingsResource
from openapi_server import util


async def service_diagnostic_settings_create_or_update(request: web.Request, resource_uri, api_version, parameters) -> web.Response:
    """service_diagnostic_settings_create_or_update

    Create or update new diagnostic settings for the specified resource. **WARNING**: This method will be deprecated in future releases.

    :param resource_uri: The identifier of the resource.
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = ServiceDiagnosticSettingsResource.from_dict(parameters)
    return web.Response(status=200)


async def service_diagnostic_settings_get(request: web.Request, resource_uri, api_version) -> web.Response:
    """service_diagnostic_settings_get

    Gets the active diagnostic settings for the specified resource. **WARNING**: This method will be deprecated in future releases.

    :param resource_uri: The identifier of the resource.
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
