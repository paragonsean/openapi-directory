from typing import List, Dict
from aiohttp import web

from openapi_server.models.continent_list import ContinentList
from openapi_server.models.country_list import CountryList
from openapi_server.models.currency_list import CurrencyList
from openapi_server.models.language_list import LanguageList
from openapi_server.models.locale import Locale
from openapi_server.models.phone_list import PhoneList
from openapi_server import util


async def locale_get(request: web.Request, ) -> web.Response:
    """Get User Locale

    Get the current user location based on IP. Returns an object with user country code, country name, continent name, continent code, ip address and suggested currency. You can use the locale header to get the data in a supported language.  ([IP Geolocation by DB-IP](https://db-ip.com))


    """
    return web.Response(status=200)


async def locale_get_continents(request: web.Request, ) -> web.Response:
    """List Continents

    List of all continents. You can use the locale header to get the data in a supported language.


    """
    return web.Response(status=200)


async def locale_get_countries(request: web.Request, ) -> web.Response:
    """List Countries

    List of all countries. You can use the locale header to get the data in a supported language.


    """
    return web.Response(status=200)


async def locale_get_countries_eu(request: web.Request, ) -> web.Response:
    """List EU Countries

    List of all countries that are currently members of the EU. You can use the locale header to get the data in a supported language.


    """
    return web.Response(status=200)


async def locale_get_countries_phones(request: web.Request, ) -> web.Response:
    """List Countries Phone Codes

    List of all countries phone codes. You can use the locale header to get the data in a supported language.


    """
    return web.Response(status=200)


async def locale_get_currencies(request: web.Request, ) -> web.Response:
    """List Currencies

    List of all currencies, including currency symbol, name, plural, and decimal digits for all major and minor currencies. You can use the locale header to get the data in a supported language.


    """
    return web.Response(status=200)


async def locale_get_languages(request: web.Request, ) -> web.Response:
    """List Languages

    List of all languages classified by ISO 639-1 including 2-letter code, name in English, and name in the respective language.


    """
    return web.Response(status=200)
