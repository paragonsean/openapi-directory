from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def gsi_besthour_0(request: web.Request, zip=None, key=None, timeframe=None, hours=None) -> web.Response:
    """Get best hour (with most regional green energy) in a given timeframe.

    Simple Wrapper around the GreenPowerIndex for easy integration into almost any SmartHome system that allows access to a JSON/REST Service This endpoint is designed to indicate if a device should be turned on or off. (Switch state). 

    :param zip: Zipcode (Postleitzahl) of a city in Germany.
    :type zip: str
    :param key: Any valid Stromkonto account (address).
    :type key: str
    :param timeframe: Number of hours to check (default 24 hours from now).
    :type timeframe: int
    :param hours: How many hours in row do you need the device turned on?
    :type hours: int

    """
    return web.Response(status=200)
