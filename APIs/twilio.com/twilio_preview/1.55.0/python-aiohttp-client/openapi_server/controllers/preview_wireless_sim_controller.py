from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_wireless_sim_response import ListWirelessSimResponse
from openapi_server.models.preview_wireless_sim import PreviewWirelessSim
from openapi_server import util


async def fetch_wireless_sim(request: web.Request, sid) -> web.Response:
    """fetch_wireless_sim

    

    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_wireless_sim(request: web.Request, status=None, iccid=None, rate_plan=None, eid=None, sim_registration_code=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_wireless_sim

    

    :param status: 
    :type status: str
    :param iccid: 
    :type iccid: str
    :param rate_plan: 
    :type rate_plan: str
    :param eid: 
    :type eid: str
    :param sim_registration_code: 
    :type sim_registration_code: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_wireless_sim(request: web.Request, sid, callback_method=None, callback_url=None, commands_callback_method=None, commands_callback_url=None, friendly_name=None, rate_plan=None, sms_fallback_method=None, sms_fallback_url=None, sms_method=None, sms_url=None, status=None, unique_name=None, voice_fallback_method=None, voice_fallback_url=None, voice_method=None, voice_url=None) -> web.Response:
    """update_wireless_sim

    

    :param sid: 
    :type sid: str
    :param callback_method: 
    :type callback_method: str
    :param callback_url: 
    :type callback_url: str
    :param commands_callback_method: 
    :type commands_callback_method: str
    :param commands_callback_url: 
    :type commands_callback_url: str
    :param friendly_name: 
    :type friendly_name: str
    :param rate_plan: 
    :type rate_plan: str
    :param sms_fallback_method: 
    :type sms_fallback_method: str
    :param sms_fallback_url: 
    :type sms_fallback_url: str
    :param sms_method: 
    :type sms_method: str
    :param sms_url: 
    :type sms_url: str
    :param status: 
    :type status: str
    :param unique_name: 
    :type unique_name: str
    :param voice_fallback_method: 
    :type voice_fallback_method: str
    :param voice_fallback_url: 
    :type voice_fallback_url: str
    :param voice_method: 
    :type voice_method: str
    :param voice_url: 
    :type voice_url: str

    """
    return web.Response(status=200)
