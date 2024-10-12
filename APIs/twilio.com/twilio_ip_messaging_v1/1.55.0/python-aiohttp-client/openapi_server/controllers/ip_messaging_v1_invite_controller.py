from typing import List, Dict
from aiohttp import web

from openapi_server.models.ip_messaging_v1_service_channel_invite import IpMessagingV1ServiceChannelInvite
from openapi_server.models.list_invite_response import ListInviteResponse
from openapi_server import util


async def create_invite(request: web.Request, service_sid, channel_sid, identity, role_sid=None) -> web.Response:
    """create_invite

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param identity: 
    :type identity: str
    :param role_sid: 
    :type role_sid: str

    """
    return web.Response(status=200)


async def delete_invite(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """delete_invite

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_invite(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """fetch_invite

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_invite(request: web.Request, service_sid, channel_sid, identity=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_invite

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param identity: 
    :type identity: List[str]
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
