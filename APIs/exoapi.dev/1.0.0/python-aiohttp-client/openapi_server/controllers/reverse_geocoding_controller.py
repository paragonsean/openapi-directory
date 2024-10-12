from typing import List, Dict
from aiohttp import web

from openapi_server.models.barcode_generator_post400_response import BarcodeGeneratorPost400Response
from openapi_server.models.reverse_geocoding_get200_response import ReverseGeocodingGet200Response
from openapi_server import util


async def reverse_geocoding_get(request: web.Request, lat, lon, locale=None) -> web.Response:
    """reverse_geocoding_get

    Quickly convert GPS coordinates to human-readable addresses

    :param lat: 
    :type lat: 
    :param lon: 
    :type lon: 
    :param locale: 
    :type locale: str

    """
    return web.Response(status=200)
