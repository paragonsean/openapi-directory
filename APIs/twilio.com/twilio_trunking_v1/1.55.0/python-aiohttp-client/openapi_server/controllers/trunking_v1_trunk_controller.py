from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_trunk_response import ListTrunkResponse
from openapi_server.models.trunk_enum_transfer_caller_id import TrunkEnumTransferCallerId
from openapi_server.models.trunk_enum_transfer_setting import TrunkEnumTransferSetting
from openapi_server.models.trunking_v1_trunk import TrunkingV1Trunk
from openapi_server import util


async def create_trunk(request: web.Request, cnam_lookup_enabled=None, disaster_recovery_method=None, disaster_recovery_url=None, domain_name=None, friendly_name=None, secure=None, transfer_caller_id=None, transfer_mode=None) -> web.Response:
    """create_trunk

    

    :param cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
    :type cnam_lookup_enabled: bool
    :param disaster_recovery_method: The HTTP method we should use to call the &#x60;disaster_recovery_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type disaster_recovery_method: str
    :param disaster_recovery_url: The URL we should call using the &#x60;disaster_recovery_method&#x60; if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
    :type disaster_recovery_url: str
    :param domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and &#x60;-&#x60; and must end with &#x60;pstn.twilio.com&#x60;. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
    :type domain_name: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param secure: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
    :type secure: bool
    :param transfer_caller_id: 
    :type transfer_caller_id: str
    :param transfer_mode: 
    :type transfer_mode: str

    """
    return web.Response(status=200)


async def delete_trunk(request: web.Request, sid) -> web.Response:
    """delete_trunk

    

    :param sid: The unique string that we created to identify the Trunk resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_trunk(request: web.Request, sid) -> web.Response:
    """fetch_trunk

    

    :param sid: The unique string that we created to identify the Trunk resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_trunk(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_trunk

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_trunk(request: web.Request, sid, cnam_lookup_enabled=None, disaster_recovery_method=None, disaster_recovery_url=None, domain_name=None, friendly_name=None, secure=None, transfer_caller_id=None, transfer_mode=None) -> web.Response:
    """update_trunk

    

    :param sid: The unique string that we created to identify the OriginationUrl resource to update.
    :type sid: str
    :param cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
    :type cnam_lookup_enabled: bool
    :param disaster_recovery_method: The HTTP method we should use to call the &#x60;disaster_recovery_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type disaster_recovery_method: str
    :param disaster_recovery_url: The URL we should call using the &#x60;disaster_recovery_method&#x60; if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
    :type disaster_recovery_url: str
    :param domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and &#x60;-&#x60; and must end with &#x60;pstn.twilio.com&#x60;. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
    :type domain_name: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param secure: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
    :type secure: bool
    :param transfer_caller_id: 
    :type transfer_caller_id: str
    :param transfer_mode: 
    :type transfer_mode: str

    """
    return web.Response(status=200)
