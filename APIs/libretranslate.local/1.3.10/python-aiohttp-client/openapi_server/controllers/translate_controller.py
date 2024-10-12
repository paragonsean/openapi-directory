from typing import List, Dict
from aiohttp import web

from openapi_server.models.detections_inner import DetectionsInner
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.error_slow_down import ErrorSlowDown
from openapi_server.models.languages_inner import LanguagesInner
from openapi_server.models.translate import Translate
from openapi_server.models.translate_file import TranslateFile
from openapi_server import util


async def detect_post(request: web.Request, ) -> web.Response:
    """Detect the language of a single text

    


    """
    return web.Response(status=200)


async def languages_get(request: web.Request, ) -> web.Response:
    """Retrieve list of supported languages

    


    """
    return web.Response(status=200)


async def translate_file_post(request: web.Request, ) -> web.Response:
    """Translate file from a language to another

    


    """
    return web.Response(status=200)


async def translate_post(request: web.Request, ) -> web.Response:
    """Translate text from a language to another

    


    """
    return web.Response(status=200)
