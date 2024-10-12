from typing import List, Dict
from aiohttp import web

from openapi_server.models.country_details_api_model import CountryDetailsApiModel
from openapi_server.models.currency_details_api_model import CurrencyDetailsApiModel
from openapi_server.models.ui_language_details_api_model import UILanguageDetailsApiModel
from openapi_server import util


async def general_api_countries(request: web.Request, x_auth_key, x_auth_secret) -> web.Response:
    """Return all of the platform supported countries

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def general_api_currencies(request: web.Request, x_auth_key, x_auth_secret) -> web.Response:
    """Return all of the platform supported currencies

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def general_api_date_formats(request: web.Request, x_auth_key, x_auth_secret) -> web.Response:
    """Return all of the platform supported Date Formats

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def general_api_ui_languages(request: web.Request, x_auth_key, x_auth_secret) -> web.Response:
    """Return all of the platform supported UI languages

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)
