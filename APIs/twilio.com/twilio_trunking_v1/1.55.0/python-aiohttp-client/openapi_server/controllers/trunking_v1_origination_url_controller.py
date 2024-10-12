from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_origination_url_response import ListOriginationUrlResponse
from openapi_server.models.trunking_v1_trunk_origination_url import TrunkingV1TrunkOriginationUrl
from openapi_server import util


async def create_origination_url(request: web.Request, trunk_sid, enabled, friendly_name, priority, sip_url, weight) -> web.Response:
    """create_origination_url

    

    :param trunk_sid: The SID of the Trunk to associate the resource with.
    :type trunk_sid: str
    :param enabled: Whether the URL is enabled. The default is &#x60;true&#x60;.
    :type enabled: bool
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
    :type priority: int
    :param sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a &#x60;sip:&#x60; schema.
    :type sip_url: str
    :param weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
    :type weight: int

    """
    return web.Response(status=200)


async def delete_origination_url(request: web.Request, trunk_sid, sid) -> web.Response:
    """delete_origination_url

    

    :param trunk_sid: The SID of the Trunk from which to delete the OriginationUrl.
    :type trunk_sid: str
    :param sid: The unique string that we created to identify the OriginationUrl resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_origination_url(request: web.Request, trunk_sid, sid) -> web.Response:
    """fetch_origination_url

    

    :param trunk_sid: The SID of the Trunk from which to fetch the OriginationUrl.
    :type trunk_sid: str
    :param sid: The unique string that we created to identify the OriginationUrl resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_origination_url(request: web.Request, trunk_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_origination_url

    

    :param trunk_sid: The SID of the Trunk from which to read the OriginationUrl.
    :type trunk_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_origination_url(request: web.Request, trunk_sid, sid, enabled=None, friendly_name=None, priority=None, sip_url=None, weight=None) -> web.Response:
    """update_origination_url

    

    :param trunk_sid: The SID of the Trunk from which to update the OriginationUrl.
    :type trunk_sid: str
    :param sid: The unique string that we created to identify the OriginationUrl resource to update.
    :type sid: str
    :param enabled: Whether the URL is enabled. The default is &#x60;true&#x60;.
    :type enabled: bool
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
    :type priority: int
    :param sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a &#x60;sip:&#x60; schema. &#x60;sips&#x60; is NOT supported.
    :type sip_url: str
    :param weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
    :type weight: int

    """
    return web.Response(status=200)
