from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.get_compay_settings_list200_response import GetCompaySettingsList200Response
from openapi_server import util


async def get_compay_settings_list(request: web.Request, name=None, description=None) -> web.Response:
    """Get a list of company settings

    

    :param name: Filter by name
    :type name: str
    :param description: Filter by description
    :type description: str

    """
    return web.Response(status=200)
