from typing import List, Dict
from aiohttp import web

from openapi_server.models.gsi_dispatch200_response import GsiDispatch200Response
from openapi_server.models.gsi_marketdata200_response import GsiMarketdata200Response
from openapi_server.models.gsi_prediction200_response import GsiPrediction200Response
from openapi_server import util


async def gsi_besthour(request: web.Request, zip=None, key=None, timeframe=None, hours=None) -> web.Response:
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


async def gsi_dispatch(request: web.Request, zip=None, key=None) -> web.Response:
    """Dispatch (Green Energy Distribution Schedule)

    Dispatch of green energy has two aspects to consider:   - Availability of gerneration facility (depends on weather and installed capacity)   - Demand of energy Using the green power index (GrünstromIndex) we have received a tool to automate distribution of energy in order to prevent redispatch situations. Doing this alows to opimize resource usage (tactical) and leverage data for investment planning (strategic). 

    :param zip: Zipcode (Postleitzahl) of a city in Germany.
    :type zip: str
    :param key: Any valid Stromkonto account (address).
    :type key: str

    """
    return web.Response(status=200)


async def gsi_marketdata(request: web.Request, zip=None) -> web.Response:
    """Marketdata

    Compatible to awattar (https://api.awattar.de/v1/marketdata) API interface but data comes from GreenPowerIndex instead of EPEXSpot. 

    :param zip: Zipcode (Postleitzahl) of a city in Germany.
    :type zip: str

    """
    return web.Response(status=200)


async def gsi_prediction(request: web.Request, zip=None, key=None) -> web.Response:
    """Prediction

    Retrieval the GreenPowerIndex (GrünstromIndex) for a given city (by zipcode) in Germany. 

    :param zip: Zipcode (Postleitzahl) of a city in Germany.
    :type zip: str
    :param key: Any valid Stromkonto account (address).
    :type key: str

    """
    return web.Response(status=200)
