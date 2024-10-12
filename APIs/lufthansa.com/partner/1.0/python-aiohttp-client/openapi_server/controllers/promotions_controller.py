from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def price_offers(request: web.Request, origin, destination, departure_date, return_date, service=None) -> web.Response:
    """Price Offers

    Retrieve a best price offer given an origin and destination.

    :param origin: Departure city. 3-letter IATA city code
    :type origin: str
    :param destination: Destination city. 3-letter IATA city code
    :type destination: str
    :param departure_date: Departure date in local time (YYYY-MM-DD)
    :type departure_date: str
    :param return_date: Return date in local time (YYYY-MM-DD)
    :type return_date: str
    :param service: Optional parameter.
    :type service: str

    """
    return web.Response(status=200)
