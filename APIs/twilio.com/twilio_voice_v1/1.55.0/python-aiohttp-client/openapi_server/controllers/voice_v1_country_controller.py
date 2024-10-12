from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_dialing_permissions_country_response import ListDialingPermissionsCountryResponse
from openapi_server.models.voice_v1_dialing_permissions_dialing_permissions_country_instance import VoiceV1DialingPermissionsDialingPermissionsCountryInstance
from openapi_server import util


async def fetch_dialing_permissions_country(request: web.Request, iso_code) -> web.Response:
    """fetch_dialing_permissions_country

    Retrieve voice dialing country permissions identified by the given ISO country code

    :param iso_code: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the DialingPermissions Country resource to fetch
    :type iso_code: str

    """
    return web.Response(status=200)


async def list_dialing_permissions_country(request: web.Request, iso_code=None, continent=None, country_code=None, low_risk_numbers_enabled=None, high_risk_special_numbers_enabled=None, high_risk_tollfraud_numbers_enabled=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_dialing_permissions_country

    Retrieve all voice dialing country permissions for this account

    :param iso_code: Filter to retrieve the country permissions by specifying the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
    :type iso_code: str
    :param continent: Filter to retrieve the country permissions by specifying the continent
    :type continent: str
    :param country_code: Filter the results by specified [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)
    :type country_code: str
    :param low_risk_numbers_enabled: Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type low_risk_numbers_enabled: bool
    :param high_risk_special_numbers_enabled: Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: &#x60;true&#x60; or &#x60;false&#x60;
    :type high_risk_special_numbers_enabled: bool
    :param high_risk_tollfraud_numbers_enabled: Filter to retrieve the country permissions with dialing to high-risk [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html) numbers enabled. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type high_risk_tollfraud_numbers_enabled: bool
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
