from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_finance_countries_get(request: web.Request, x_api_key=None) -> web.Response:
    """Get available countries

    

    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_finance_crypto_address_get(request: web.Request, crypto_type=None, x_api_key=None) -> web.Response:
    """Get crypto address

    

    :param crypto_type: 
    :type crypto_type: str
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_finance_crypto_address_types_get(request: web.Request, x_api_key=None) -> web.Response:
    """Get available crypto types

    

    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_finance_iban_country_code_get(request: web.Request, country_code, x_api_key=None) -> web.Response:
    """Get IBAN by countryCode

    

    :param country_code: 
    :type country_code: str
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_finance_vat_validator_post(request: web.Request, country, vat, x_api_key=None) -> web.Response:
    """api_finance_vat_validator_post

    

    :param country: 
    :type country: str
    :param vat: 
    :type vat: str
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)
