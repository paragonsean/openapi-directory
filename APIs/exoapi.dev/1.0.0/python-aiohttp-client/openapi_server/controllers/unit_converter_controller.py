from typing import List, Dict
from aiohttp import web

from openapi_server.models.barcode_generator_post400_response import BarcodeGeneratorPost400Response
from openapi_server.models.unit_converter_get200_response import UnitConverterGet200Response
from openapi_server import util


async def unit_converter_get(request: web.Request, _from, to, value) -> web.Response:
    """unit_converter_get

    Quickly convert between all different kinds of measurement units

    :param _from: 
    :type _from: str
    :param to: 
    :type to: str
    :param value: 
    :type value: 

    """
    return web.Response(status=200)
