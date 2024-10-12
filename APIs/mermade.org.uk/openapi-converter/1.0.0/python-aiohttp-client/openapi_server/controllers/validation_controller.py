from typing import List, Dict
from aiohttp import web

from openapi_server.models.validation_result import ValidationResult
from openapi_server import util


async def get_badge(request: web.Request, url) -> web.Response:
    """Return a redirect to a badge svg file depending on a source definition&#39;s validity

    

    :param url: The URL to retrieve the OpenAPI 3.0.x definition from
    :type url: str

    """
    return web.Response(status=200)


async def validate(request: web.Request, filename=None, source=None) -> web.Response:
    """Validate an OpenAPI 3.0.x definition supplied in the body of the request

    

    :param filename: The file to upload and validate
    :type filename: str
    :param source: The text of an OpenAPI 3.0.x definition to validate
    :type source: str

    """
    return web.Response(status=200)


async def validate_url(request: web.Request, url) -> web.Response:
    """Validate an OpenAPI 3.0.x definition

    

    :param url: The URL to retrieve the OpenAPI 3.0.x definition from
    :type url: str

    """
    return web.Response(status=200)
