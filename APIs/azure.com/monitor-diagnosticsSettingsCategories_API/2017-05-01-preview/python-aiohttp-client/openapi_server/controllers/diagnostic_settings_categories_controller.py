from typing import List, Dict
from aiohttp import web

from openapi_server.models.diagnostic_settings_category_resource import DiagnosticSettingsCategoryResource
from openapi_server.models.diagnostic_settings_category_resource_collection import DiagnosticSettingsCategoryResourceCollection
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def diagnostic_settings_category_get(request: web.Request, resource_uri, api_version, name) -> web.Response:
    """diagnostic_settings_category_get

    Gets the diagnostic settings category for the specified resource.

    :param resource_uri: The identifier of the resource.
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param name: The name of the diagnostic setting.
    :type name: str

    """
    return web.Response(status=200)


async def diagnostic_settings_category_list(request: web.Request, resource_uri, api_version) -> web.Response:
    """diagnostic_settings_category_list

    Lists the diagnostic settings categories for the specified resource.

    :param resource_uri: The identifier of the resource.
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
