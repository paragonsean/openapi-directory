from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_available_phone_number_country import ApiV2010AccountAvailablePhoneNumberCountry
from openapi_server.models.list_available_phone_number_country_response import ListAvailablePhoneNumberCountryResponse
from openapi_server import util


async def fetch_available_phone_number_country(request: web.Request, account_sid, country_code) -> web.Response:
    """fetch_available_phone_number_country

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the available phone number Country resource.
    :type account_sid: str
    :param country_code: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country to fetch available phone number information about.
    :type country_code: str

    """
    return web.Response(status=200)


async def list_available_phone_number_country(request: web.Request, account_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_available_phone_number_country

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the available phone number Country resources.
    :type account_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
