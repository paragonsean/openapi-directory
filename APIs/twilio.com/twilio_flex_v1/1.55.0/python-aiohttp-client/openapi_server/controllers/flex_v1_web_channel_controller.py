from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_web_channel import FlexV1WebChannel
from openapi_server.models.list_web_channel_response import ListWebChannelResponse
from openapi_server.models.web_channel_enum_chat_status import WebChannelEnumChatStatus
from openapi_server import util


async def create_web_channel(request: web.Request, chat_friendly_name, customer_friendly_name, flex_flow_sid, identity, chat_unique_name=None, pre_engagement_data=None) -> web.Response:
    """create_web_channel

    

    :param chat_friendly_name: The chat channel&#39;s friendly name.
    :type chat_friendly_name: str
    :param customer_friendly_name: The chat participant&#39;s friendly name.
    :type customer_friendly_name: str
    :param flex_flow_sid: The SID of the Flex Flow.
    :type flex_flow_sid: str
    :param identity: The chat identity.
    :type identity: str
    :param chat_unique_name: The chat channel&#39;s unique name.
    :type chat_unique_name: str
    :param pre_engagement_data: The pre-engagement data.
    :type pre_engagement_data: str

    """
    return web.Response(status=200)


async def delete_web_channel(request: web.Request, sid) -> web.Response:
    """delete_web_channel

    

    :param sid: The SID of the WebChannel resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_web_channel(request: web.Request, sid) -> web.Response:
    """fetch_web_channel

    

    :param sid: The SID of the WebChannel resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_web_channel(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_web_channel

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_web_channel(request: web.Request, sid, chat_status=None, post_engagement_data=None) -> web.Response:
    """update_web_channel

    

    :param sid: The SID of the WebChannel resource to update.
    :type sid: str
    :param chat_status: 
    :type chat_status: str
    :param post_engagement_data: The post-engagement data.
    :type post_engagement_data: str

    """
    return web.Response(status=200)
