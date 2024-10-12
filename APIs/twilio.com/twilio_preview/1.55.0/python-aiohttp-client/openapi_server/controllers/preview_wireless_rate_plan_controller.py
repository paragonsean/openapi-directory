from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_wireless_rate_plan_response import ListWirelessRatePlanResponse
from openapi_server.models.preview_wireless_rate_plan import PreviewWirelessRatePlan
from openapi_server import util


async def create_wireless_rate_plan(request: web.Request, commands_enabled=None, data_enabled=None, data_limit=None, data_metering=None, friendly_name=None, international_roaming=None, messaging_enabled=None, national_roaming_enabled=None, unique_name=None, voice_enabled=None) -> web.Response:
    """create_wireless_rate_plan

    

    :param commands_enabled: 
    :type commands_enabled: bool
    :param data_enabled: 
    :type data_enabled: bool
    :param data_limit: 
    :type data_limit: int
    :param data_metering: 
    :type data_metering: str
    :param friendly_name: 
    :type friendly_name: str
    :param international_roaming: 
    :type international_roaming: List[str]
    :param messaging_enabled: 
    :type messaging_enabled: bool
    :param national_roaming_enabled: 
    :type national_roaming_enabled: bool
    :param unique_name: 
    :type unique_name: str
    :param voice_enabled: 
    :type voice_enabled: bool

    """
    return web.Response(status=200)


async def delete_wireless_rate_plan(request: web.Request, sid) -> web.Response:
    """delete_wireless_rate_plan

    

    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_wireless_rate_plan(request: web.Request, sid) -> web.Response:
    """fetch_wireless_rate_plan

    

    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_wireless_rate_plan(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_wireless_rate_plan

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_wireless_rate_plan(request: web.Request, sid, friendly_name=None, unique_name=None) -> web.Response:
    """update_wireless_rate_plan

    

    :param sid: 
    :type sid: str
    :param friendly_name: 
    :type friendly_name: str
    :param unique_name: 
    :type unique_name: str

    """
    return web.Response(status=200)
