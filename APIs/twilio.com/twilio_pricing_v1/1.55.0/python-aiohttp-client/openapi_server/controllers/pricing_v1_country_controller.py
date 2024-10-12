from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_messaging_country_response import ListMessagingCountryResponse
from openapi_server.models.list_phone_number_country_response import ListPhoneNumberCountryResponse
from openapi_server.models.list_voice_country_response import ListVoiceCountryResponse
from openapi_server.models.pricing_v1_messaging_messaging_country_instance import PricingV1MessagingMessagingCountryInstance
from openapi_server.models.pricing_v1_phone_number_phone_number_country_instance import PricingV1PhoneNumberPhoneNumberCountryInstance
from openapi_server.models.pricing_v1_voice_voice_country_instance import PricingV1VoiceVoiceCountryInstance
from openapi_server import util


async def fetch_messaging_country(request: web.Request, iso_country) -> web.Response:
    """fetch_messaging_country

    

    :param iso_country: The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the pricing information to fetch.
    :type iso_country: str

    """
    return web.Response(status=200)


async def fetch_phone_number_country(request: web.Request, iso_country) -> web.Response:
    """fetch_phone_number_country

    

    :param iso_country: The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the pricing information to fetch.
    :type iso_country: str

    """
    return web.Response(status=200)


async def fetch_voice_country(request: web.Request, iso_country) -> web.Response:
    """fetch_voice_country

    

    :param iso_country: The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the pricing information to fetch.
    :type iso_country: str

    """
    return web.Response(status=200)


async def list_messaging_country(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_messaging_country

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def list_phone_number_country(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_phone_number_country

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def list_voice_country(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_voice_country

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
