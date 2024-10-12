from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_sip_sip_domain import ApiV2010AccountSipSipDomain
from openapi_server.models.list_sip_domain_response import ListSipDomainResponse
from openapi_server import util


async def create_sip_domain(request: web.Request, account_sid, domain_name, byoc_trunk_sid=None, emergency_caller_sid=None, emergency_calling_enabled=None, friendly_name=None, secure=None, sip_registration=None, voice_fallback_method=None, voice_fallback_url=None, voice_method=None, voice_status_callback_method=None, voice_status_callback_url=None, voice_url=None) -> web.Response:
    """create_sip_domain

    Create a new Domain

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    :type account_sid: str
    :param domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\&quot;-\\\&quot; and must end with &#x60;sip.twilio.com&#x60;.
    :type domain_name: str
    :param byoc_trunk_sid: The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with.
    :type byoc_trunk_sid: str
    :param emergency_caller_sid: Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call.
    :type emergency_caller_sid: str
    :param emergency_calling_enabled: Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses.
    :type emergency_calling_enabled: bool
    :param friendly_name: A descriptive string that you created to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param secure: Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain.
    :type secure: bool
    :param sip_registration: Whether to allow SIP Endpoints to register with the domain to receive calls. Can be &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; allows SIP Endpoints to register with the domain to receive calls, &#x60;false&#x60; does not.
    :type sip_registration: bool
    :param voice_fallback_method: The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type voice_fallback_method: str
    :param voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;voice_url&#x60;.
    :type voice_fallback_url: str
    :param voice_method: The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type voice_method: str
    :param voice_status_callback_method: The HTTP method we should use to call &#x60;voice_status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type voice_status_callback_method: str
    :param voice_status_callback_url: The URL that we should call to pass status parameters (such as call ended) to your application.
    :type voice_status_callback_url: str
    :param voice_url: The URL we should when the domain receives a call.
    :type voice_url: str

    """
    return web.Response(status=200)


async def delete_sip_domain(request: web.Request, account_sid, sid) -> web.Response:
    """delete_sip_domain

    Delete an instance of a Domain

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to delete.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the SipDomain resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sip_domain(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_sip_domain

    Fetch an instance of a Domain

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the SipDomain resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sip_domain(request: web.Request, account_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sip_domain

    Retrieve a list of domains belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to read.
    :type account_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sip_domain(request: web.Request, account_sid, sid, byoc_trunk_sid=None, domain_name=None, emergency_caller_sid=None, emergency_calling_enabled=None, friendly_name=None, secure=None, sip_registration=None, voice_fallback_method=None, voice_fallback_url=None, voice_method=None, voice_status_callback_method=None, voice_status_callback_url=None, voice_url=None) -> web.Response:
    """update_sip_domain

    Update the attributes of a domain

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to update.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the SipDomain resource to update.
    :type sid: str
    :param byoc_trunk_sid: The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with.
    :type byoc_trunk_sid: str
    :param domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\&quot;-\\\&quot; and must end with &#x60;sip.twilio.com&#x60;.
    :type domain_name: str
    :param emergency_caller_sid: Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call.
    :type emergency_caller_sid: str
    :param emergency_calling_enabled: Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses.
    :type emergency_calling_enabled: bool
    :param friendly_name: A descriptive string that you created to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param secure: Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain.
    :type secure: bool
    :param sip_registration: Whether to allow SIP Endpoints to register with the domain to receive calls. Can be &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; allows SIP Endpoints to register with the domain to receive calls, &#x60;false&#x60; does not.
    :type sip_registration: bool
    :param voice_fallback_method: The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type voice_fallback_method: str
    :param voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML requested by &#x60;voice_url&#x60;.
    :type voice_fallback_url: str
    :param voice_method: The HTTP method we should use to call &#x60;voice_url&#x60;
    :type voice_method: str
    :param voice_status_callback_method: The HTTP method we should use to call &#x60;voice_status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type voice_status_callback_method: str
    :param voice_status_callback_url: The URL that we should call to pass status parameters (such as call ended) to your application.
    :type voice_status_callback_url: str
    :param voice_url: The URL we should call when the domain receives a call.
    :type voice_url: str

    """
    return web.Response(status=200)
