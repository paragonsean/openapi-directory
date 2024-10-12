from typing import List, Dict
from aiohttp import web

from openapi_server.models.diagnostic_settings_category_resource_collection import DiagnosticSettingsCategoryResourceCollection
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def diagnostic_settings_category_list(request: web.Request, api_version) -> web.Response:
    """diagnostic_settings_category_list

    Lists the diagnostic settings categories for AadIam.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
