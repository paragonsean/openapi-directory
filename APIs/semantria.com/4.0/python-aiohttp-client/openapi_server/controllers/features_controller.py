from typing import List, Dict
from aiohttp import web

from openapi_server.models.feature import Feature
from openapi_server import util


async def get_features(request: web.Request, content_type, language=None) -> web.Response:
    """Retrieve supported features

    This method returns list of supported features per languages supported by Semantria API. Let the users know about API capabilities.

    :param content_type: 
    :type content_type: str
    :param language: Filter features by specified language
    :type language: str

    """
    return web.Response(status=200)
