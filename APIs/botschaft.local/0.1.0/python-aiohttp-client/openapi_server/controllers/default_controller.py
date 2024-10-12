from typing import List, Dict
from aiohttp import web

from openapi_server.models.config import Config
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def config_config_get(request: web.Request, authorization=None) -> web.Response:
    """Config

    

    :param authorization: 
    :type authorization: str

    """
    return web.Response(status=200)


async def topic_topic_topic_name_get(request: web.Request, topic_name, message=None, base64_message=None, authorization=None) -> web.Response:
    """Topic

    

    :param topic_name: 
    :type topic_name: str
    :param message: 
    :type message: str
    :param base64_message: 
    :type base64_message: str
    :param authorization: 
    :type authorization: str

    """
    return web.Response(status=200)
