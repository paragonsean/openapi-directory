from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def wards_in_a_district(request: web.Request, country, region, district) -> web.Response:
    """Returns all wards in a district

    Returns all wards in a  specified district and district postcode

    :param country: Country name in lowercase eg( tanzania)
    :type country: str
    :param region: Name of the region eg (Mbeya)
    :type region: str
    :param district: Name of the District eg (Rungwe)
    :type district: str

    """
    return web.Response(status=200)
