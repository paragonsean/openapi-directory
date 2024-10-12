from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_application import ApiV2010AccountApplication
from openapi_server.models.list_application_response import ListApplicationResponse
from openapi_server import util


async def create_application(request: web.Request, account_sid, api_version=None, friendly_name=None, message_status_callback=None, public_application_connect_enabled=None, sms_fallback_method=None, sms_fallback_url=None, sms_method=None, sms_status_callback=None, sms_url=None, status_callback=None, status_callback_method=None, voice_caller_id_lookup=None, voice_fallback_method=None, voice_fallback_url=None, voice_method=None, voice_url=None) -> web.Response:
    """create_application

    Create a new application within your account

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    :type account_sid: str
    :param api_version: The API version to use to start a new TwiML session. Can be: &#x60;2010-04-01&#x60; or &#x60;2008-08-01&#x60;. The default value is the account&#39;s default API version.
    :type api_version: str
    :param friendly_name: A descriptive string that you create to describe the new application. It can be up to 64 characters long.
    :type friendly_name: str
    :param message_status_callback: The URL we should call using a POST method to send message status information to your application.
    :type message_status_callback: str
    :param public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type public_application_connect_enabled: bool
    :param sms_fallback_method: The HTTP method we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type sms_fallback_method: str
    :param sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;.
    :type sms_fallback_url: str
    :param sms_method: The HTTP method we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type sms_method: str
    :param sms_status_callback: The URL we should call using a POST method to send status information about SMS messages sent by the application.
    :type sms_status_callback: str
    :param sms_url: The URL we should call when the phone number receives an incoming SMS message.
    :type sms_url: str
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application.
    :type status_callback: str
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type status_callback_method: str
    :param voice_caller_id_lookup: Whether we should look up the caller&#39;s caller-ID name from the CNAM database (additional charges apply). Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type voice_caller_id_lookup: bool
    :param voice_fallback_method: The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type voice_fallback_method: str
    :param voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;.
    :type voice_fallback_url: str
    :param voice_method: The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type voice_method: str
    :param voice_url: The URL we should call when the phone number assigned to this application receives a call.
    :type voice_url: str

    """
    return web.Response(status=200)


async def delete_application(request: web.Request, account_sid, sid) -> web.Response:
    """delete_application

    Delete the application by the specified application sid

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to delete.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Application resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_application(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_application

    Fetch the application specified by the provided sid

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resource to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Application resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_application(request: web.Request, account_sid, friendly_name=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_application

    Retrieve a list of applications representing an application within the requesting account

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to read.
    :type account_sid: str
    :param friendly_name: The string that identifies the Application resources to read.
    :type friendly_name: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_application(request: web.Request, account_sid, sid, api_version=None, friendly_name=None, message_status_callback=None, public_application_connect_enabled=None, sms_fallback_method=None, sms_fallback_url=None, sms_method=None, sms_status_callback=None, sms_url=None, status_callback=None, status_callback_method=None, voice_caller_id_lookup=None, voice_fallback_method=None, voice_fallback_url=None, voice_method=None, voice_url=None) -> web.Response:
    """update_application

    Updates the application&#39;s properties

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to update.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Application resource to update.
    :type sid: str
    :param api_version: The API version to use to start a new TwiML session. Can be: &#x60;2010-04-01&#x60; or &#x60;2008-08-01&#x60;. The default value is your account&#39;s default API version.
    :type api_version: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param message_status_callback: The URL we should call using a POST method to send message status information to your application.
    :type message_status_callback: str
    :param public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type public_application_connect_enabled: bool
    :param sms_fallback_method: The HTTP method we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type sms_fallback_method: str
    :param sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;.
    :type sms_fallback_url: str
    :param sms_method: The HTTP method we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type sms_method: str
    :param sms_status_callback: Same as message_status_callback: The URL we should call using a POST method to send status information about SMS messages sent by the application. Deprecated, included for backwards compatibility.
    :type sms_status_callback: str
    :param sms_url: The URL we should call when the phone number receives an incoming SMS message.
    :type sms_url: str
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application.
    :type status_callback: str
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type status_callback_method: str
    :param voice_caller_id_lookup: Whether we should look up the caller&#39;s caller-ID name from the CNAM database (additional charges apply). Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type voice_caller_id_lookup: bool
    :param voice_fallback_method: The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type voice_fallback_method: str
    :param voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;.
    :type voice_fallback_url: str
    :param voice_method: The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type voice_method: str
    :param voice_url: The URL we should call when the phone number assigned to this application receives a call.
    :type voice_url: str

    """
    return web.Response(status=200)
