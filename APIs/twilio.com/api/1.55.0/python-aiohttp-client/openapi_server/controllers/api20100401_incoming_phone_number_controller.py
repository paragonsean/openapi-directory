from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_incoming_phone_number import ApiV2010AccountIncomingPhoneNumber
from openapi_server.models.incoming_phone_number_enum_emergency_status import IncomingPhoneNumberEnumEmergencyStatus
from openapi_server.models.incoming_phone_number_enum_voice_receive_mode import IncomingPhoneNumberEnumVoiceReceiveMode
from openapi_server.models.list_incoming_phone_number_response import ListIncomingPhoneNumberResponse
from openapi_server import util


async def create_incoming_phone_number(request: web.Request, account_sid, address_sid=None, api_version=None, area_code=None, bundle_sid=None, emergency_address_sid=None, emergency_status=None, friendly_name=None, identity_sid=None, phone_number=None, sms_application_sid=None, sms_fallback_method=None, sms_fallback_url=None, sms_method=None, sms_url=None, status_callback=None, status_callback_method=None, trunk_sid=None, voice_application_sid=None, voice_caller_id_lookup=None, voice_fallback_method=None, voice_fallback_url=None, voice_method=None, voice_receive_mode=None, voice_url=None) -> web.Response:
    """create_incoming_phone_number

    Purchase a phone-number for the account.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    :type account_sid: str
    :param address_sid: The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.
    :type address_sid: str
    :param api_version: The API version to use for incoming calls made to the new phone number. The default is &#x60;2010-04-01&#x60;.
    :type api_version: str
    :param area_code: The desired area code for your new incoming phone number. Can be any three-digit, US or Canada area code. We will provision an available phone number within this area code for you. **You must provide an &#x60;area_code&#x60; or a &#x60;phone_number&#x60;.** (US and Canada only).
    :type area_code: str
    :param bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
    :type bundle_sid: str
    :param emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the new phone number.
    :type emergency_address_sid: str
    :param emergency_status: 
    :type emergency_status: str
    :param friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the new phone number.
    :type friendly_name: str
    :param identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations.
    :type identity_sid: str
    :param phone_number: The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
    :type phone_number: str
    :param sms_application_sid: The SID of the application that should handle SMS messages sent to the new phone number. If an &#x60;sms_application_sid&#x60; is present, we ignore all of the &#x60;sms_*_url&#x60; urls and use those set on the application.
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


async def delete_incoming_phone_number(request: web.Request, account_sid, sid) -> web.Response:
    """delete_incoming_phone_number

    Delete a phone-numbers belonging to the account used to make the request.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resources to delete.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_incoming_phone_number(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_incoming_phone_number

    Fetch an incoming-phone-number belonging to the account used to make the request.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_incoming_phone_number(request: web.Request, account_sid, beta=None, friendly_name=None, phone_number=None, origin=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_incoming_phone_number

    Retrieve a list of incoming-phone-numbers belonging to the account used to make the request.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resources to read.
    :type account_sid: str
    :param beta: Whether to include phone numbers new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;.
    :type beta: bool
    :param friendly_name: A string that identifies the IncomingPhoneNumber resources to read.
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


async def update_incoming_phone_number(request: web.Request, account_sid, sid, account_sid2=None, address_sid=None, api_version=None, bundle_sid=None, emergency_address_sid=None, emergency_status=None, friendly_name=None, identity_sid=None, sms_application_sid=None, sms_fallback_method=None, sms_fallback_url=None, sms_method=None, sms_url=None, status_callback=None, status_callback_method=None, trunk_sid=None, voice_application_sid=None, voice_caller_id_lookup=None, voice_fallback_method=None, voice_fallback_url=None, voice_method=None, voice_receive_mode=None, voice_url=None) -> web.Response:
    """update_incoming_phone_number

    Update an incoming-phone-number instance.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to update.  For more information, see [Exchanging Numbers Between Subaccounts](https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers).
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to update.
    :type sid: str
    :param account_sid2: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to update.  For more information, see [Exchanging Numbers Between Subaccounts](https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers).
    :type account_sid2: str
    :param address_sid: The SID of the Address resource we should associate with the phone number. Some regions require addresses to meet local regulations.
    :type address_sid: str
    :param api_version: The API version to use for incoming calls made to the phone number. The default is &#x60;2010-04-01&#x60;.
    :type api_version: str
    :param bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
    :type bundle_sid: str
    :param emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from this phone number.
    :type emergency_address_sid: str
    :param emergency_status: 
    :type emergency_status: str
    :param friendly_name: A descriptive string that you created to describe this phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number.
    :type friendly_name: str
    :param identity_sid: The SID of the Identity resource that we should associate with the phone number. Some regions require an identity to meet local regulations.
    :type identity_sid: str
    :param sms_application_sid: The SID of the application that should handle SMS messages sent to the number. If an &#x60;sms_application_sid&#x60; is present, we ignore all of the &#x60;sms_*_url&#x60; urls and use those set on the application.
    :type sms_application_sid: str
    :param sms_fallback_method: The HTTP method that we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type sms_fallback_method: str
    :param sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML defined by &#x60;sms_url&#x60;.
    :type sms_fallback_url: str
    :param sms_method: The HTTP method that we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type sms_method: str
    :param sms_url: The URL we should call when the phone number receives an incoming SMS message.
    :type sms_url: str
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application.
    :type status_callback: str
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type status_callback_method: str
    :param trunk_sid: The SID of the Trunk we should use to handle phone calls to the phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa.
    :type trunk_sid: str
    :param voice_application_sid: The SID of the application we should use to handle phone calls to the phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice urls and use only those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa.
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
    :param voice_url: The URL that we should call to answer a call to the phone number. The &#x60;voice_url&#x60; will not be called if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set.
    :type voice_url: str

    """
    return web.Response(status=200)
