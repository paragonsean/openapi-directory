from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_unauthorized import AccountUnauthorized
from openapi_server.models.available_numbers import AvailableNumbers
from openapi_server.models.inbound_numbers import InboundNumbers
from openapi_server.models.response import Response
from openapi_server.models.response420 import Response420
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def buy_a_number(request: web.Request, country, msisdn, target_api_key=None) -> web.Response:
    """Buy a number

    Request to purchase a specific inbound number.

    :param country: The two character country code in ISO 3166-1 alpha-2 format
    :type country: str
    :param msisdn: An available inbound virtual number.
    :type msisdn: str
    :param target_api_key: If you’d like to perform an action on a subaccount, provide the &#x60;api_key&#x60; of that account here. If you’d like to perform an action on your own account, you do not need to provide this field.
    :type target_api_key: str

    """
    return web.Response(status=200)


async def cancel_a_number(request: web.Request, country, msisdn, target_api_key=None) -> web.Response:
    """Cancel a number

    Cancel your subscription for a specific inbound number.

    :param country: The two character country code in ISO 3166-1 alpha-2 format
    :type country: str
    :param msisdn: An available inbound virtual number.
    :type msisdn: str
    :param target_api_key: If you’d like to perform an action on a subaccount, provide the &#x60;api_key&#x60; of that account here. If you’d like to perform an action on your own account, you do not need to provide this field.
    :type target_api_key: str

    """
    return web.Response(status=200)


async def get_available_numbers(request: web.Request, country, type=None, pattern=None, search_pattern=None, features=None, size=None, index=None) -> web.Response:
    """Search available numbers

    Retrieve inbound numbers that are available for the specified country.

    :param country: The two character country code to filter on (in ISO 3166-1 alpha-2 format)
    :type country: str
    :param type: Set this parameter to filter the type of number, such as mobile or landline
    :type type: str
    :param pattern: The number pattern you want to search for. Use in conjunction with &#x60;search_pattern&#x60;.
    :type pattern: str
    :param search_pattern: The strategy you want to use for matching:   * &#x60;0&#x60; - Search for numbers that start with &#x60;pattern&#x60; (Note: all numbers are in E.164 format, so the starting pattern includes the country code, such as 1 for USA) * &#x60;1&#x60; - Search for numbers that contain &#x60;pattern&#x60; * &#x60;2&#x60; - Search for numbers that end with &#x60;pattern&#x60; 
    :type search_pattern: int
    :param features: Available features are &#x60;SMS&#x60;, &#x60;VOICE&#x60; and &#x60;MMS&#x60;. To look for numbers that support multiple features, use a comma-separated value: &#x60;SMS,MMS,VOICE&#x60;.
    :type features: str
    :param size: Page size
    :type size: int
    :param index: Page index
    :type index: int

    """
    return web.Response(status=200)


async def get_owned_numbers(request: web.Request, application_id=None, has_application=None, country=None, pattern=None, search_pattern=None, size=None, index=None) -> web.Response:
    """List the numbers you own

    Retrieve all the inbound numbers associated with your Vonage account.

    :param application_id: The Application that you want to return the numbers for.
    :type application_id: str
    :param has_application: Set this optional field to &#x60;true&#x60; to restrict your results to numbers associated with an Application (any Application). Set to &#x60;false&#x60; to find all numbers not associated with any Application. Omit the field to avoid filtering on whether or not the number is assigned to an Application. 
    :type has_application: bool
    :param country: 
    :type country: str
    :param pattern: The number pattern you want to search for. Use in conjunction with &#x60;search_pattern&#x60;.
    :type pattern: str
    :param search_pattern: The strategy you want to use for matching:   * &#x60;0&#x60; - Search for numbers that start with &#x60;pattern&#x60; (Note: all numbers are in E.164 format, so the starting pattern includes the country code, such as 1 for USA) * &#x60;1&#x60; - Search for numbers that contain &#x60;pattern&#x60; * &#x60;2&#x60; - Search for numbers that end with &#x60;pattern&#x60; 
    :type search_pattern: int
    :param size: Page size
    :type size: int
    :param index: Page index
    :type index: int

    """
    return web.Response(status=200)


async def update_a_number(request: web.Request, country, msisdn, app_id=None, messages_callback_type=None, messages_callback_value=None, mo_http_url=None, mo_smpp_sys_type=None, voice_callback_type=None, voice_callback_value=None, voice_status_callback=None) -> web.Response:
    """Update a number

    Change the behaviour of a number that you own.

    :param country: The two character country code in ISO 3166-1 alpha-2 format
    :type country: str
    :param msisdn: An available inbound virtual number.
    :type msisdn: str
    :param app_id: The Application that will handle inbound traffic to this number.
    :type app_id: str
    :param messages_callback_type: &lt;strong&gt;DEPRECATED&lt;/strong&gt; - We recommend that you use &#x60;app_id&#x60; instead.  Specifies the Messages webhook type (always &#x60;app&#x60;) associated with this number and must be used with the &#x60;messagesCallbackValue&#x60; parameter. 
    :type messages_callback_type: str
    :param messages_callback_value: &lt;strong&gt;DEPRECATED&lt;/strong&gt; - We recommend that you use &#x60;app_id&#x60; instead.  Specifies the Application ID of your Messages application. It must be used with the &#x60;messagesCallbackType&#x60; parameter. 
    :type messages_callback_value: str
    :param mo_http_url: An URL-encoded URI to the webhook endpoint that handles inbound messages. Your webhook endpoint must be active before you make this request. Vonage makes a &#x60;GET&#x60; request to the endpoint and checks that it returns a &#x60;200 OK&#x60; response. Set this parameter&#39;s value to an empty string to remove the webhook.
    :type mo_http_url: str
    :param mo_smpp_sys_type: The associated system type for your SMPP client
    :type mo_smpp_sys_type: str
    :param voice_callback_type: Specify whether inbound voice calls on your number are forwarded to a SIP or a telephone number.  This must be used with the &#x60;voiceCallbackValue&#x60; parameter. If set, &#x60;sip&#x60; or &#x60;tel&#x60; are prioritized over the Voice capability in your Application.  *Note: The &#x60;app&#x60; value is deprecated and will be removed in future.* 
    :type voice_callback_type: str
    :param voice_callback_value: A SIP URI or telephone number. Must be used with the &#x60;voiceCallbackType&#x60; parameter.
    :type voice_callback_value: str
    :param voice_status_callback: A webhook URI for Vonage to send a request to when a call ends
    :type voice_status_callback: str

    """
    return web.Response(status=200)
