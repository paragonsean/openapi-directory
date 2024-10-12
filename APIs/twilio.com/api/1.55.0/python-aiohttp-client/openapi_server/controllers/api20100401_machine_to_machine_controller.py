from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_available_phone_number_machine_to_machine_response import ListAvailablePhoneNumberMachineToMachineResponse
from openapi_server import util


async def list_available_phone_number_machine_to_machine(request: web.Request, account_sid, country_code, area_code=None, contains=None, sms_enabled=None, mms_enabled=None, voice_enabled=None, exclude_all_address_required=None, exclude_local_address_required=None, exclude_foreign_address_required=None, beta=None, near_number=None, near_lat_long=None, distance=None, in_postal_code=None, in_region=None, in_rate_center=None, in_lata=None, in_locality=None, fax_enabled=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_available_phone_number_machine_to_machine

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources.
    :type account_sid: str
    :param country_code: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers.
    :type country_code: str
    :param area_code: The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada.
    :type area_code: int
    :param contains: The pattern on which to match phone numbers. Valid characters are &#x60;*&#x60;, &#x60;0-9&#x60;, &#x60;a-z&#x60;, and &#x60;A-Z&#x60;. The &#x60;*&#x60; character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters.
    :type contains: str
    :param sms_enabled: Whether the phone numbers can receive text messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type sms_enabled: bool
    :param mms_enabled: Whether the phone numbers can receive MMS messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type mms_enabled: bool
    :param voice_enabled: Whether the phone numbers can receive calls. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type voice_enabled: bool
    :param exclude_all_address_required: Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;.
    :type exclude_all_address_required: bool
    :param exclude_local_address_required: Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;.
    :type exclude_local_address_required: bool
    :param exclude_foreign_address_required: Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;.
    :type exclude_foreign_address_required: bool
    :param beta: Whether to read phone numbers that are new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;.
    :type beta: bool
    :param near_number: Given a phone number, find a geographically close number within &#x60;distance&#x60; miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada.
    :type near_number: str
    :param near_lat_long: Given a latitude/longitude pair &#x60;lat,long&#x60; find geographically close numbers within &#x60;distance&#x60; miles. Applies to only phone numbers in the US and Canada.
    :type near_lat_long: str
    :param distance: The search radius, in miles, for a &#x60;near_&#x60; query.  Can be up to &#x60;500&#x60; and the default is &#x60;25&#x60;. Applies to only phone numbers in the US and Canada.
    :type distance: int
    :param in_postal_code: Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada.
    :type in_postal_code: str
    :param in_region: Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada.
    :type in_region: str
    :param in_rate_center: Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires &#x60;in_lata&#x60; to be set as well. Applies to only phone numbers in the US and Canada.
    :type in_rate_center: str
    :param in_lata: Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada.
    :type in_lata: str
    :param in_locality: Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number.
    :type in_locality: str
    :param fax_enabled: Whether the phone numbers can receive faxes. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type fax_enabled: bool
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
