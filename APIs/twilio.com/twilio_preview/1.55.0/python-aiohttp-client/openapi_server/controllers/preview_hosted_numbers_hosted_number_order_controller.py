from typing import List, Dict
from aiohttp import web

from openapi_server.models.hosted_number_order_enum_status import HostedNumberOrderEnumStatus
from openapi_server.models.hosted_number_order_enum_verification_type import HostedNumberOrderEnumVerificationType
from openapi_server.models.list_hosted_numbers_hosted_number_order_response import ListHostedNumbersHostedNumberOrderResponse
from openapi_server.models.preview_hosted_numbers_hosted_number_order import PreviewHostedNumbersHostedNumberOrder
from openapi_server import util


async def create_hosted_numbers_hosted_number_order(request: web.Request, phone_number, sms_capability, account_sid=None, address_sid=None, cc_emails=None, email=None, friendly_name=None, sms_application_sid=None, sms_fallback_method=None, sms_fallback_url=None, sms_method=None, sms_url=None, status_callback_method=None, status_callback_url=None, unique_name=None, verification_document_sid=None, verification_type=None) -> web.Response:
    """create_hosted_numbers_hosted_number_order

    Host a phone number&#39;s capability on Twilio&#39;s platform.

    :param phone_number: The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format
    :type phone_number: str
    :param sms_capability: Used to specify that the SMS capability will be hosted on Twilio&#39;s platform.
    :type sms_capability: bool
    :param account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to.
    :type account_sid: str
    :param address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number.
    :type address_sid: str
    :param cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to.
    :type cc_emails: List[str]
    :param email: Optional. Email of the owner of this phone number that is being hosted.
    :type email: str
    :param friendly_name: A 64 character string that is a human readable text that describes this resource.
    :type friendly_name: str
    :param sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a &#x60;SmsApplicationSid&#x60; is present, Twilio will ignore all of the SMS urls above and use those set on the application.
    :type sms_application_sid: str
    :param sms_fallback_method: The HTTP method that should be used to request the SmsFallbackUrl. Must be either &#x60;GET&#x60; or &#x60;POST&#x60;. This will be copied onto the IncomingPhoneNumber resource.
    :type sms_fallback_method: str
    :param sms_fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
    :type sms_fallback_url: str
    :param sms_method: The HTTP method that should be used to request the SmsUrl. Must be either &#x60;GET&#x60; or &#x60;POST&#x60;.  This will be copied onto the IncomingPhoneNumber resource.
    :type sms_method: str
    :param sms_url: The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the IncomingPhoneNumber resource.
    :type sms_url: str
    :param status_callback_method: Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
    :type status_callback_method: str
    :param status_callback_url: Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
    :type status_callback_url: str
    :param unique_name: Optional. Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
    :type unique_name: str
    :param verification_document_sid: Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill.
    :type verification_document_sid: str
    :param verification_type: 
    :type verification_type: str

    """
    return web.Response(status=200)


async def delete_hosted_numbers_hosted_number_order(request: web.Request, sid) -> web.Response:
    """delete_hosted_numbers_hosted_number_order

    Cancel the HostedNumberOrder (only available when the status is in &#x60;received&#x60;).

    :param sid: A 34 character string that uniquely identifies this HostedNumberOrder.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_hosted_numbers_hosted_number_order(request: web.Request, sid) -> web.Response:
    """fetch_hosted_numbers_hosted_number_order

    Fetch a specific HostedNumberOrder.

    :param sid: A 34 character string that uniquely identifies this HostedNumberOrder.
    :type sid: str

    """
    return web.Response(status=200)


async def list_hosted_numbers_hosted_number_order(request: web.Request, status=None, phone_number=None, incoming_phone_number_sid=None, friendly_name=None, unique_name=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_hosted_numbers_hosted_number_order

    Retrieve a list of HostedNumberOrders belonging to the account initiating the request.

    :param status: The Status of this HostedNumberOrder. One of &#x60;received&#x60;, &#x60;pending-verification&#x60;, &#x60;verified&#x60;, &#x60;pending-loa&#x60;, &#x60;carrier-processing&#x60;, &#x60;testing&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, or &#x60;action-required&#x60;.
    :type status: str
    :param phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
    :type phone_number: str
    :param incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
    :type incoming_phone_number_sid: str
    :param friendly_name: A human readable description of this resource, up to 64 characters.
    :type friendly_name: str
    :param unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
    :type unique_name: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_hosted_numbers_hosted_number_order(request: web.Request, sid, call_delay=None, cc_emails=None, email=None, extension=None, friendly_name=None, status=None, unique_name=None, verification_code=None, verification_document_sid=None, verification_type=None) -> web.Response:
    """update_hosted_numbers_hosted_number_order

    Updates a specific HostedNumberOrder.

    :param sid: A 34 character string that uniquely identifies this HostedNumberOrder.
    :type sid: str
    :param call_delay: The number of seconds, between 0 and 60, to delay before initiating the verification call. Defaults to 0.
    :type call_delay: int
    :param cc_emails: Optional. A list of emails that LOA document for this HostedNumberOrder will be carbon copied to.
    :type cc_emails: List[str]
    :param email: Email of the owner of this phone number that is being hosted.
    :type email: str
    :param extension: Digits to dial after connecting the verification call.
    :type extension: str
    :param friendly_name: A 64 character string that is a human readable text that describes this resource.
    :type friendly_name: str
    :param status: 
    :type status: str
    :param unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
    :type unique_name: str
    :param verification_code: A verification code that is given to the user via a phone call to the phone number that is being hosted.
    :type verification_code: str
    :param verification_document_sid: Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill.
    :type verification_document_sid: str
    :param verification_type: 
    :type verification_type: str

    """
    return web.Response(status=200)
