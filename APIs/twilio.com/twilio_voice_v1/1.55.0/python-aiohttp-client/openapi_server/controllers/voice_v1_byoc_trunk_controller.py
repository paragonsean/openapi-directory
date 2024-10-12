from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_byoc_trunk_response import ListByocTrunkResponse
from openapi_server.models.voice_v1_byoc_trunk import VoiceV1ByocTrunk
from openapi_server import util


async def create_byoc_trunk(request: web.Request, cnam_lookup_enabled=None, connection_policy_sid=None, friendly_name=None, from_domain_sid=None, status_callback_method=None, status_callback_url=None, voice_fallback_method=None, voice_fallback_url=None, voice_method=None, voice_url=None) -> web.Response:
    """create_byoc_trunk

    

    :param cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
    :type cnam_lookup_enabled: bool
    :param connection_policy_sid: The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
    :type connection_policy_sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str
    :param from_domain_sid: The SID of the SIP Domain that should be used in the &#x60;From&#x60; header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\&quot;call back\\\&quot; an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\&quot;sip.twilio.com\\\&quot;.
    :type from_domain_sid: str
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type status_callback_method: str
    :param status_callback_url: The URL that we should call to pass status parameters (such as call ended) to your application.
    :type status_callback_url: str
    :param voice_fallback_method: The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type voice_fallback_method: str
    :param voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;voice_url&#x60;.
    :type voice_fallback_url: str
    :param voice_method: The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type voice_method: str
    :param voice_url: The URL we should call when the BYOC Trunk receives a call.
    :type voice_url: str

    """
    return web.Response(status=200)


async def delete_byoc_trunk(request: web.Request, sid) -> web.Response:
    """delete_byoc_trunk

    

    :param sid: The Twilio-provided string that uniquely identifies the BYOC Trunk resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_byoc_trunk(request: web.Request, sid) -> web.Response:
    """fetch_byoc_trunk

    

    :param sid: The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_byoc_trunk(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_byoc_trunk

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_byoc_trunk(request: web.Request, sid, cnam_lookup_enabled=None, connection_policy_sid=None, friendly_name=None, from_domain_sid=None, status_callback_method=None, status_callback_url=None, voice_fallback_method=None, voice_fallback_url=None, voice_method=None, voice_url=None) -> web.Response:
    """update_byoc_trunk

    

    :param sid: The Twilio-provided string that uniquely identifies the BYOC Trunk resource to update.
    :type sid: str
    :param cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
    :type cnam_lookup_enabled: bool
    :param connection_policy_sid: The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
    :type connection_policy_sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str
    :param from_domain_sid: The SID of the SIP Domain that should be used in the &#x60;From&#x60; header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\&quot;call back\\\&quot; an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\&quot;sip.twilio.com\\\&quot;.
    :type from_domain_sid: str
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type status_callback_method: str
    :param status_callback_url: The URL that we should call to pass status parameters (such as call ended) to your application.
    :type status_callback_url: str
    :param voice_fallback_method: The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type voice_fallback_method: str
    :param voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML requested by &#x60;voice_url&#x60;.
    :type voice_fallback_url: str
    :param voice_method: The HTTP method we should use to call &#x60;voice_url&#x60;
    :type voice_method: str
    :param voice_url: The URL we should call when the BYOC Trunk receives a call.
    :type voice_url: str

    """
    return web.Response(status=200)
