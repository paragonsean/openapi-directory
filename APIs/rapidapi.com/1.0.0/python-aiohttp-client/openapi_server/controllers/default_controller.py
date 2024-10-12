from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_advanced_moon_phase_data200_response import GetAdvancedMoonPhaseData200Response
from openapi_server.models.get_basic_moon_phase_data200_response import GetBasicMoonPhaseData200Response
from openapi_server import util


async def get_advanced_moon_phase_data(request: web.Request, filters=None, x_rapidapi_key=None) -> web.Response:
    """Get Advanced Moon Phase Data

    Get Advanced Moon Phase Data

    :param filters: Filter data in the Advanced Moon API by specifying the desired fields using the &#x60;filters&#x60; parameter in the request. Include a comma-separated list of keys to retrieve customized data, allowing you to fetch specific moon phase information and related details.
    :type filters: str
    :param x_rapidapi_key: 
    :type x_rapidapi_key: str

    """
    return web.Response(status=200)


async def get_basic_moon_phase_data(request: web.Request, x_rapidapi_key=None) -> web.Response:
    """Get Basic Moon Phase Data

    Get Basic Moon Phase Data

    :param x_rapidapi_key: 
    :type x_rapidapi_key: str

    """
    return web.Response(status=200)


async def get_emoji_of_moon_phase(request: web.Request, x_rapidapi_key=None) -> web.Response:
    """Get Emoji of Moon Phase

    Get Emoji of Moon Phase

    :param x_rapidapi_key: 
    :type x_rapidapi_key: str

    """
    return web.Response(status=200)


async def get_lunar_calendar(request: web.Request, filters=None, x_rapidapi_key=None) -> web.Response:
    """Get Lunar Calendar

    Get Lunar Calendar

    :param filters: Filter data in the Advanced Moon API by specifying the desired fields using the &#x60;filters&#x60; parameter in the request. Include a comma-separated list of keys to retrieve customized data, allowing you to fetch specific moon phase information and related details.
    :type filters: str
    :param x_rapidapi_key: 
    :type x_rapidapi_key: str

    """
    return web.Response(status=200)


async def get_plain_text_moon_phase_data(request: web.Request, x_rapidapi_key=None) -> web.Response:
    """Get Plain Text Moon Phase Data

    Get Plain Text Moon Phase Data

    :param x_rapidapi_key: 
    :type x_rapidapi_key: str

    """
    return web.Response(status=200)
