from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_wireless_command_response import ListWirelessCommandResponse
from openapi_server.models.preview_wireless_command import PreviewWirelessCommand
from openapi_server import util


async def create_wireless_command(request: web.Request, command, callback_method=None, callback_url=None, command_mode=None, device=None, include_sid=None, sim=None) -> web.Response:
    """create_wireless_command

    

    :param command: 
    :type command: str
    :param callback_method: 
    :type callback_method: str
    :param callback_url: 
    :type callback_url: str
    :param command_mode: 
    :type command_mode: str
    :param device: 
    :type device: str
    :param include_sid: 
    :type include_sid: str
    :param sim: 
    :type sim: str

    """
    return web.Response(status=200)


async def fetch_wireless_command(request: web.Request, sid) -> web.Response:
    """fetch_wireless_command

    

    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_wireless_command(request: web.Request, device=None, sim=None, status=None, direction=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_wireless_command

    

    :param device: 
    :type device: str
    :param sim: 
    :type sim: str
    :param status: 
    :type status: str
    :param direction: 
    :type direction: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
