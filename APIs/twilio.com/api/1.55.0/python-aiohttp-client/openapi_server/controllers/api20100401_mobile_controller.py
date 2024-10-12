from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_incoming_phone_number_incoming_phone_number_mobile import ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberMobile
from openapi_server.models.incoming_phone_number_mobile_enum_emergency_status import IncomingPhoneNumberMobileEnumEmergencyStatus
from openapi_server.models.incoming_phone_number_mobile_enum_voice_receive_mode import IncomingPhoneNumberMobileEnumVoiceReceiveMode
from openapi_server.models.list_available_phone_number_mobile_response import ListAvailablePhoneNumberMobileResponse
from openapi_server.models.list_incoming_phone_number_mobile_response import ListIncomingPhoneNumberMobileResponse
from openapi_server import util


async def create_incoming_phone_number_mobile(request: web.Request, account_sid, phone_number, address_sid=None, api_version=None, bundle_sid=None, emergency_address_sid=None, emergency_status=None, friendly_name=None, identity_sid=None, sms_application_sid=None, sms_fallback_method=None, sms_fallback_url=None, sms_method=None, sms_url=None, status_callback=None, status_callback_method=None, trunk_sid=None, voice_application_sid=None, voice_caller_id_lookup=None, voice_fallback_method=None, voice_fallback_url=None, voice_method=None, voice_receive_mode=None, voice_url=None) -> web.Response:
    """create_incoming_phone_number_mobile

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    :type account_sid: str
    :param phone_number: The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
    :type phone_number: str
    :param address_sid: The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.
    :type address_sid: str
    :param api_version: The API version to use for incoming calls made to the new phone number. The default is &#x60;2010-04-01&#x60;.
    :type api_version: str
    :param bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
    :type bundle_sid: str
    :param emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the new phone number.
    :type emergency_address_sid: str
    :param emergency_status: 
    :type emergency_status: str
    :param friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, the is a formatted version of the phone number.
    :type friendly_name: str
    :param identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations.
    :type identity_sid: str
    :param sms_application_sid: The SID of the application that should handle SMS messages sent to the new phone number. If an &#x60;sms_application_sid&#x60; is present, we ignore all of the &#x60;sms_*_url&#x60; urls and use those of the application.
    :type sms_application_sid: str
    :param sms_fallback_method: The HTTP method that we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type sms_fallback_method: str
    :param sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML defined by &#x60;sms_url&#x60;.
    :type sms_fallback_url: str
    :param sms_method: The HTTP method that we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type sms_method: str
    :param sms_url: The URL we should call when the new phone number receives an incoming SMS message.
    :type sms_url: str
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application.
    :type status_callback: str
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type status_callback_method: str
    :param trunk_sid: The SID of the Trunk we should use to handle calls to the new phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa.
    :type trunk_sid: str
    :param voice_application_sid: The SID of the application we should use to handle calls to the new phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice urls and use only those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa.
    :type voice_application_sid: str
    :param voice_caller_id_lookup: Whether to lookup the caller&#39;s name from the CNAM database and post it to your app. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;.
    :type voice_caller_id_lookup: bool
    :param voice_fallback_method: The HTTP method that we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type voice_fallback_method: str
    :param voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;.
    :type voice_fallback_url: str
    :param voice_method: The HTTP method that we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type voice_method: str
    :param voice_receive_mode: 
    :type voice_receive_mode: str
    :param voice_url: The URL that we should call to answer a call to the new phone number. The &#x60;voice_url&#x60; will not be called if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set.
    :type voice_url: str

    """
    return web.Response(status=200)


async def list_available_phone_number_mobile(request: web.Request, account_sid, country_code, area_code=None, contains=None, sms_enabled=None, mms_enabled=None, voice_enabled=None, exclude_all_address_required=None, exclude_local_address_required=None, exclude_foreign_address_required=None, beta=None, near_number=None, near_lat_long=None, distance=None, in_postal_code=None, in_region=None, in_rate_center=None, in_lata=None, in_locality=None, fax_enabled=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_available_phone_number_mobile

    

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


async def list_incoming_phone_number_mobile(request: web.Request, account_sid, beta=None, friendly_name=None, phone_number=None, origin=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_incoming_phone_number_mobile

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
    :type account_sid: str
    :param beta: Whether to include phone numbers new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;.
    :type beta: bool
    :param friendly_name: A string that identifies the resources to read.
    :type friendly_name: str
    :param phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use &#39;*&#39; as a wildcard for any digit.
    :type phone_number: str
    :param origin: Whether to include phone numbers based on their origin. Can be: &#x60;twilio&#x60; or &#x60;hosted&#x60;. By default, phone numbers of all origin are included.
    :type origin: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
