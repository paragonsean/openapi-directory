from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def neighborhood_in_a_street(request: web.Request, country, region, district, ward, street) -> web.Response:
    """Returns all neighborhood in a street

    Returns all neighborhood in a specified street

    :param country: Country name in lowercase eg( tanzania)
    :type country: str
    :param region: Name of the region eg (Mbeya)
    :type region: str
    :param district: Name of the District eg (Rungwe)
    :type district: str
    :param ward: Name of the Ward eg (Kiwira)
    :type ward: str
    :param street: Name of the Street eg (Ilundo)
    :type street: str

    """
    return web.Response(status=200)
