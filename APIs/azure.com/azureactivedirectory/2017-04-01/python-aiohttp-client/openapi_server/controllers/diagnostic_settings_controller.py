from typing import List, Dict
from aiohttp import web

from openapi_server.models.diagnostic_settings_resource import DiagnosticSettingsResource
from openapi_server.models.diagnostic_settings_resource_collection import DiagnosticSettingsResourceCollection
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def diagnostic_settings_create_or_update(request: web.Request, api_version, name, parameters) -> web.Response:
    """diagnostic_settings_create_or_update

    Creates or updates diagnostic settings for AadIam.

    :param api_version: Client Api Version.
    :type api_version: str
    :param name: The name of the diagnostic setting.
    :type name: str
    :param parameters: Parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = DiagnosticSettingsResource.from_dict(parameters)
    return web.Response(status=200)


async def diagnostic_settings_delete(request: web.Request, api_version, name) -> web.Response:
    """diagnostic_settings_delete

    Deletes existing diagnostic setting for AadIam.

    :param api_version: Client Api Version.
    :type api_version: str
    :param name: The name of the diagnostic setting.
    :type name: str

    """
    return web.Response(status=200)


async def diagnostic_settings_get(request: web.Request, api_version, name) -> web.Response:
    """diagnostic_settings_get

    Gets the active diagnostic setting for AadIam.

    :param api_version: Client Api Version.
    :type api_version: str
    :param name: The name of the diagnostic setting.
    :type name: str

    """
    return web.Response(status=200)


async def diagnostic_settings_list(request: web.Request, api_version) -> web.Response:
    """diagnostic_settings_list

    Gets the active diagnostic settings list for AadIam.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
