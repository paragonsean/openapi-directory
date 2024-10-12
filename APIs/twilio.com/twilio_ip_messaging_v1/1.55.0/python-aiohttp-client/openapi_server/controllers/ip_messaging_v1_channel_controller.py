from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel_enum_channel_type import ChannelEnumChannelType
from openapi_server.models.ip_messaging_v1_service_channel import IpMessagingV1ServiceChannel
from openapi_server.models.list_channel_response import ListChannelResponse
from openapi_server import util


async def create_channel(request: web.Request, service_sid, attributes=None, friendly_name=None, type=None, unique_name=None) -> web.Response:
    """create_channel

    

    :param service_sid: 
    :type service_sid: str
    :param attributes: 
    :type attributes: str
    :param friendly_name: 
    :type friendly_name: str
    :param type: 
    :type type: str
    :param unique_name: 
    :type unique_name: str

    """
    return web.Response(status=200)


async def delete_channel(request: web.Request, service_sid, sid) -> web.Response:
    """delete_channel

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_channel(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_channel

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_channel(request: web.Request, service_sid, type=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_channel

    

    :param service_sid: 
    :type service_sid: str
    :param type: 
    :type type: list | bytes
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    type = [ChannelEnumChannelType.from_dict(d) for d in type]
    return web.Response(status=200)


async def update_channel(request: web.Request, service_sid, sid, attributes=None, friendly_name=None, unique_name=None) -> web.Response:
    """update_channel

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str
    :param attributes: 
    :type attributes: str
    :param friendly_name: 
    :type friendly_name: str
    :param unique_name: 
    :type unique_name: str

    """
    return web.Response(status=200)
