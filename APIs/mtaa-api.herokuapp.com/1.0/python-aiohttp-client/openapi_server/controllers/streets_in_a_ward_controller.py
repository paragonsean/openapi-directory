from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def streets_in_a_ward(request: web.Request, country, region, district, ward) -> web.Response:
    """Returns all streets in a ward

    Returns all streets in a specified ward and ward postcode

    :param country: Country name in lowercase eg( tanzania)
    :type country: str
    :param region: Name of the region eg (Mbeya)
    :type region: str
    :param district: Name of the District eg (Rungwe)
    :type district: str
    :param ward: Name of the Ward eg (Kiwira)
    :type ward: str

    """
    return web.Response(status=200)
