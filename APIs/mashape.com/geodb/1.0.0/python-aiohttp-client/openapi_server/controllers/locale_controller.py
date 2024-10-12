from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.currencies_response import CurrenciesResponse
from openapi_server.models.date_time_response import DateTimeResponse
from openapi_server.models.forbidden_response import ForbiddenResponse
from openapi_server.models.languages_response import LanguagesResponse
from openapi_server.models.locales_response import LocalesResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.time_response import TimeResponse
from openapi_server.models.time_zone_response import TimeZoneResponse
from openapi_server.models.time_zones_response import TimeZonesResponse
from openapi_server import util


async def get_currencies_using_get(request: web.Request, country_id, hateoas_mode=None, limit=None, offset=None) -> web.Response:
    """Find currencies

    Find currencies, filtering by optional criteria. If no criteria are set, you will get back all known currencies.

    :param country_id: Currencies for this country id
    :type country_id: str
    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int

    """
    return web.Response(status=200)


async def get_languages_using_get(request: web.Request, hateoas_mode=None, limit=None, offset=None) -> web.Response:
    """Get languages

    Get all supported languages

    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int

    """
    return web.Response(status=200)


async def get_locales_using_get(request: web.Request, hateoas_mode=None, limit=None, offset=None) -> web.Response:
    """Get locales

    Get all known locales

    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int

    """
    return web.Response(status=200)


async def get_time_zone_date_time_using_get(request: web.Request, zone_id) -> web.Response:
    """Get time-zone date-time

    Get time-zone date-time

    :param zone_id: A time-zone id
    :type zone_id: str

    """
    return web.Response(status=200)


async def get_time_zone_time_using_get(request: web.Request, zone_id) -> web.Response:
    """Get time-zone time

    Get time-zone time

    :param zone_id: A time-zone id
    :type zone_id: str

    """
    return web.Response(status=200)


async def get_time_zone_using_get(request: web.Request, zone_id) -> web.Response:
    """Get time-zone

    Get time-zone

    :param zone_id: A time-zone id
    :type zone_id: str

    """
    return web.Response(status=200)


async def get_timezones_using_get(request: web.Request, hateoas_mode=None, limit=None, offset=None) -> web.Response:
    """Get time-zones

    Get all known time-zones

    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int

    """
    return web.Response(status=200)
