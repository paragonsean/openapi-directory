from typing import List, Dict
from aiohttp import web

from openapi_server.models.input_part import InputPart
from openapi_server import util


async def auto_complete(request: web.Request, text=None, sources=None, layers=None, country_code=None, size=None) -> web.Response:
    """Search

    Return search results in json

    :param text: 
    :type text: str
    :param sources: 
    :type sources: str
    :param layers: 
    :type layers: str
    :param country_code: 
    :type country_code: str
    :param size: 
    :type size: int

    """
    return web.Response(status=200)


async def get_reverse_geo_code(request: web.Request, lat=None, lng=None) -> web.Response:
    """Get reverse geocoding

    Return search results in json

    :param lat: 
    :type lat: float
    :param lng: 
    :type lng: float

    """
    return web.Response(status=200)


async def search(request: web.Request, text=None, sources=None, layers=None, country_code=None, size=None) -> web.Response:
    """Get geocoding

    Return search results in json

    :param text: 
    :type text: str
    :param sources: 
    :type sources: str
    :param layers: 
    :type layers: str
    :param country_code: 
    :type country_code: str
    :param size: 
    :type size: int

    """
    return web.Response(status=200)


async def search_coordinates(request: web.Request, coordinates=None) -> web.Response:
    """Search coordinates in different formate

    Return search results in json

    :param coordinates: 
    :type coordinates: str

    """
    return web.Response(status=200)


async def upload_file(request: web.Request, type=None, form_data=None, form_data_map=None, parts=None, preamble=None) -> web.Response:
    """Batch upload

    Upload csv file with minimum two columns (Id, SourceLocality). Return search results in json

    :param type: 
    :type type: str
    :param form_data: 
    :type form_data: dict | bytes
    :param form_data_map: 
    :type form_data_map: dict | bytes
    :param parts: 
    :type parts: list | bytes
    :param preamble: 
    :type preamble: str

    """
    form_data = {k: InputPart.from_dict(v) for k, v in form_data}
    form_data_map = {k: List.from_dict(v) for k, v in form_data_map}
    parts = [InputPart.from_dict(d) for d in parts]
    return web.Response(status=200)
