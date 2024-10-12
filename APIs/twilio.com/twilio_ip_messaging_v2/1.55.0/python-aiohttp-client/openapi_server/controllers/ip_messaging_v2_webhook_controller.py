from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel_webhook_enum_method import ChannelWebhookEnumMethod
from openapi_server.models.channel_webhook_enum_type import ChannelWebhookEnumType
from openapi_server.models.ip_messaging_v2_service_channel_channel_webhook import IpMessagingV2ServiceChannelChannelWebhook
from openapi_server.models.list_channel_webhook_response import ListChannelWebhookResponse
from openapi_server import util


async def create_channel_webhook(request: web.Request, service_sid, channel_sid, type, configuration_filters=None, configuration_flow_sid=None, configuration_method=None, configuration_retry_count=None, configuration_triggers=None, configuration_url=None) -> web.Response:
    """create_channel_webhook

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param type: 
    :type type: str
    :param configuration_filters: 
    :type configuration_filters: List[str]
    :param configuration_flow_sid: 
    :type configuration_flow_sid: str
    :param configuration_method: 
    :type configuration_method: str
    :param configuration_retry_count: 
    :type configuration_retry_count: int
    :param configuration_triggers: 
    :type configuration_triggers: List[str]
    :param configuration_url: 
    :type configuration_url: str

    """
    return web.Response(status=200)


async def delete_channel_webhook(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """delete_channel_webhook

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_channel_webhook(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """fetch_channel_webhook

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_channel_webhook(request: web.Request, service_sid, channel_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_channel_webhook

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_channel_webhook(request: web.Request, service_sid, channel_sid, sid, configuration_filters=None, configuration_flow_sid=None, configuration_method=None, configuration_retry_count=None, configuration_triggers=None, configuration_url=None) -> web.Response:
    """update_channel_webhook

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param sid: 
    :type sid: str
    :param configuration_filters: 
    :type configuration_filters: List[str]
    :param configuration_flow_sid: 
    :type configuration_flow_sid: str
    :param configuration_method: 
    :type configuration_method: str
    :param configuration_retry_count: 
    :type configuration_retry_count: int
    :param configuration_triggers: 
    :type configuration_triggers: List[str]
    :param configuration_url: 
    :type configuration_url: str

    """
    return web.Response(status=200)
