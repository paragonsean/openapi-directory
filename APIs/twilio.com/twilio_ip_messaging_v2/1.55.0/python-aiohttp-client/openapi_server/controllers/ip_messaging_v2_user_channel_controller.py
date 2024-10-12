from typing import List, Dict
from aiohttp import web

from openapi_server.models.ip_messaging_v2_service_user_user_channel import IpMessagingV2ServiceUserUserChannel
from openapi_server.models.list_user_channel_response import ListUserChannelResponse
from openapi_server.models.user_channel_enum_notification_level import UserChannelEnumNotificationLevel
from openapi_server import util


async def delete_user_channel(request: web.Request, service_sid, user_sid, channel_sid) -> web.Response:
    """delete_user_channel

    

    :param service_sid: 
    :type service_sid: str
    :param user_sid: 
    :type user_sid: str
    :param channel_sid: 
    :type channel_sid: str

    """
    return web.Response(status=200)


async def fetch_user_channel(request: web.Request, service_sid, user_sid, channel_sid) -> web.Response:
    """fetch_user_channel

    

    :param service_sid: 
    :type service_sid: str
    :param user_sid: 
    :type user_sid: str
    :param channel_sid: 
    :type channel_sid: str

    """
    return web.Response(status=200)


async def list_user_channel(request: web.Request, service_sid, user_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_user_channel

    

    :param service_sid: 
    :type service_sid: str
    :param user_sid: 
    :type user_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_user_channel(request: web.Request, service_sid, user_sid, channel_sid, last_consumed_message_index=None, last_consumption_timestamp=None, notification_level=None) -> web.Response:
    """update_user_channel

    

    :param service_sid: 
    :type service_sid: str
    :param user_sid: 
    :type user_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param last_consumed_message_index: 
    :type last_consumed_message_index: int
    :param last_consumption_timestamp: 
    :type last_consumption_timestamp: str
    :param notification_level: 
    :type notification_level: str

    """
    last_consumption_timestamp = util.deserialize_datetime(last_consumption_timestamp)
    return web.Response(status=200)
