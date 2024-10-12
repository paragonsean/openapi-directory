from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def cabwise_get(request: web.Request, lat, lon, optype=None, wc=None, radius=None, name=None, max_results=None, legacy_format=None, force_xml=None, twenty_four_seven_only=None) -> web.Response:
    """Gets taxis and minicabs contact information

    

    :param lat: Latitude
    :type lat: float
    :param lon: Longitude
    :type lon: float
    :param optype: Operator Type e.g Minicab, Executive, Limousine
    :type optype: str
    :param wc: Wheelchair accessible
    :type wc: str
    :param radius: The radius of the bounding circle in metres
    :type radius: float
    :param name: Trading name of operating company
    :type name: str
    :param max_results: An optional parameter to limit the number of results return. Default and maximum is 20.
    :type max_results: int
    :param legacy_format: Legacy Format
    :type legacy_format: bool
    :param force_xml: Force Xml
    :type force_xml: bool
    :param twenty_four_seven_only: Twenty Four Seven Only
    :type twenty_four_seven_only: bool

    """
    return web.Response(status=200)
