from typing import List, Dict
from aiohttp import web

from openapi_server.models.addresses import Addresses
from openapi_server.models.countries import Countries
from openapi_server.models.country import Country
from openapi_server.models.currencies import Currencies
from openapi_server.models.currency import Currency
from openapi_server.models.locations_errors import LocationsErrors
from openapi_server import util


async def address_lookup(request: web.Request, house_num, post_code) -> web.Response:
    """address_lookup

    Retrieves a list of addresses when supplied with a house number or name and a postcode. It is generally used during customer registration to provide a list of possible addresses from where the customer can select their own address details. 

    :param house_num: House number or name of the address.
    :type house_num: str
    :param post_code: Postcode of the address, no spaces required.
    :type post_code: str

    """
    return web.Response(status=200)


async def get_countries(request: web.Request, ) -> web.Response:
    """get_countries

    Retrieves a list of countries and its currencies.


    """
    return web.Response(status=200)


async def get_country(request: web.Request, country_code) -> web.Response:
    """get_country

    Retrieves the specified country and its currency.

    :param country_code: Code of the country
    :type country_code: str

    """
    return web.Response(status=200)


async def get_currencies(request: web.Request, ) -> web.Response:
    """get_currencies

    Retreives the list of currencies.


    """
    return web.Response(status=200)


async def get_currency(request: web.Request, currency_code) -> web.Response:
    """get_currency

    Retreives the specified currency.

    :param currency_code: Code of the currency
    :type currency_code: str

    """
    return web.Response(status=200)
