from typing import List, Dict
from aiohttp import web

from openapi_server.models.componentsh0 import Componentsh0
from openapi_server.models.tariffh0 import Tariffh0
from openapi_server import util


async def tariff_slph0(request: web.Request, zipcode=None) -> web.Response:
    """Energy Tariff information

    Provides pricing data for private households with standard load profiles (Standardlastprofil H0). 

    :param zipcode: Zipcode (Postzleitzahl) of a city in Germany.
    :type zipcode: str

    """
    return web.Response(status=200)


async def tariffcomponents(request: web.Request, zipcode=None, email=None, kwha=None, milliseconds=None, wh=None) -> web.Response:
    """Energy Tariff price components

    Provides insides into the different cost components of energy for a private household. Sample Request: https://api.corrently.io/v2.0/tariff/components?email&#x3D;demo%40corrently.io&amp;zip&#x3D;69168&amp;kwha&#x3D;3300 

    :param zipcode: Zipcode (Postzleitzahl) of a city in Germany.
    :type zipcode: str
    :param email: Valid email address to assign request to (pre offer generation). Ensure GDPR (DSGVO) at any time
    :type email: str
    :param kwha: Total amount of energy in kilo-watt-hours per year. (sample 2100)
    :type kwha: int
    :param milliseconds: If provided all results will be scaled to this timeframe
    :type milliseconds: int
    :param wh: If provided together with milliseconds, a cost component stament for a particular event (like charging a car) will be created.
    :type wh: int

    """
    return web.Response(status=200)
