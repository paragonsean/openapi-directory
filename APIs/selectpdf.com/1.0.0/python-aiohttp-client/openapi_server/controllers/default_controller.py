from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversion_parameters import ConversionParameters
from openapi_server import util


async def api2_convert_post(request: web.Request, parameters=None) -> web.Response:
    """Performs a html to pdf conversion

    Converts provided HTML string or url to PDF

    :param parameters: Conversion parameters
    :type parameters: dict | bytes

    """
    parameters = ConversionParameters.from_dict(parameters)
    return web.Response(status=200)
