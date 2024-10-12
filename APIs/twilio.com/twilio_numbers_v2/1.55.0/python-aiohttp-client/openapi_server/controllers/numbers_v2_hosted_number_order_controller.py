from typing import List, Dict
from aiohttp import web

from openapi_server.models.hosted_number_order_enum_status import HostedNumberOrderEnumStatus
from openapi_server.models.list_hosted_number_order_response import ListHostedNumberOrderResponse
from openapi_server.models.numbers_v2_hosted_number_order import NumbersV2HostedNumberOrder
from openapi_server import util


async def create_hosted_number_order(request: web.Request, address_sid, contact_phone_number, email, phone_number, account_sid=None, cc_emails=None, contact_title=None, friendly_name=None, sms_application_sid=None, sms_capability=None, sms_fallback_method=None, sms_fallback_url=None, sms_method=None, sms_url=None, status_callback_method=None, status_callback_url=None) -> web.Response:
    """create_hosted_number_order

    Host a phone number&#39;s capability on Twilio&#39;s platform.

    :param address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number.
    :type address_sid: str
    :param contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
    :type contact_phone_number: str
    :param email: Optional. Email of the owner of this phone number that is being hosted.
    :type email: str
    :param phone_number: The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format
    :type phone_number: str
    :param account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to.
    :type account_sid: str
    :param cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to.
    :type cc_emails: List[str]
    :param contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
    :type contact_title: str
    :param friendly_name: A 128 character string that is a human readable text that describes this resource.
    :type friendly_name: str
    :param sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a &#x60;SmsApplicationSid&#x60; is present, Twilio will ignore all of the SMS urls above and use those set on the application.
    :type sms_application_sid: str
    :param sms_capability: Used to specify that the SMS capability will be hosted on Twilio&#39;s platform.
    :type sms_capability: bool
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

    """
    return web.Response(status=200)


async def delete_hosted_number_order(request: web.Request, sid) -> web.Response:
    """delete_hosted_number_order

    Cancel the HostedNumberOrder (only available when the status is in &#x60;received&#x60;).

    :param sid: A 34 character string that uniquely identifies this HostedNumberOrder.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_hosted_number_order(request: web.Request, sid) -> web.Response:
    """fetch_hosted_number_order

    Fetch a specific HostedNumberOrder.

    :param sid: A 34 character string that uniquely identifies this HostedNumberOrder.
    :type sid: str

    """
    return web.Response(status=200)


async def list_hosted_number_order(request: web.Request, status=None, sms_capability=None, phone_number=None, incoming_phone_number_sid=None, friendly_name=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_hosted_number_order

    Retrieve a list of HostedNumberOrders belonging to the account initiating the request.

    :param status: The Status of this HostedNumberOrder. One of &#x60;received&#x60;, &#x60;pending-verification&#x60;, &#x60;verified&#x60;, &#x60;pending-loa&#x60;, &#x60;carrier-processing&#x60;, &#x60;testing&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, or &#x60;action-required&#x60;.
    :type status: str
    :param sms_capability: Whether the SMS capability will be hosted on our platform. Can be &#x60;true&#x60; of &#x60;false&#x60;.
    :type sms_capability: bool
    :param phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
    :type phone_number: str
    :param incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
    :type incoming_phone_number_sid: str
    :param friendly_name: A human readable description of this resource, up to 128 characters.
    :type friendly_name: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
