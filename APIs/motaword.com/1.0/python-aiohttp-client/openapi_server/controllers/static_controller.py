from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.formats import Formats
from openapi_server.models.language import Language
from openapi_server import util


async def get_endpoints(request: web.Request, ) -> web.Response:
    """Available endpoints

    The root endpoint will provide you with an OpenAPI definition of MotaWord API. 


    """
    return web.Response(status=200)


async def get_formats(request: web.Request, ) -> web.Response:
    """List of supported file formats

    Get a list of supported formats for documents, style guides and extensions. 


    """
    return web.Response(status=200)


async def get_languages(request: web.Request, ) -> web.Response:
    """List of supported languages

    Get a list of supported languages


    """
    return web.Response(status=200)


async def get_swagger_yaml(request: web.Request, ) -> web.Response:
    """OpenAPI YAML representation of our API

    Get Swagger YAML


    """
    return web.Response(status=200)
