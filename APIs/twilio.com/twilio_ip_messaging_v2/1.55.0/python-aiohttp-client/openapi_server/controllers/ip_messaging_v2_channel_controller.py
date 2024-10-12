from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel_enum_channel_type import ChannelEnumChannelType
from openapi_server.models.channel_enum_webhook_enabled_type import ChannelEnumWebhookEnabledType
from openapi_server.models.ip_messaging_v2_service_channel import IpMessagingV2ServiceChannel
from openapi_server.models.list_channel_response import ListChannelResponse
from openapi_server import util


async def create_channel(request: web.Request, service_sid, x_twilio_webhook_enabled=None, attributes=None, created_by=None, date_created=None, date_updated=None, friendly_name=None, type=None, unique_name=None) -> web.Response:
    """create_channel

    

    :param service_sid: 
    :type service_sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: 
    :type attributes: str
    :param created_by: 
    :type created_by: str
    :param date_created: 
    :type date_created: str
    :param date_updated: 
    :type date_updated: str
    :param friendly_name: 
    :type friendly_name: str
    :param type: 
    :type type: str
    :param unique_name: 
    :type unique_name: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def delete_channel(request: web.Request, service_sid, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_channel

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

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


async def update_channel(request: web.Request, service_sid, sid, x_twilio_webhook_enabled=None, attributes=None, created_by=None, date_created=None, date_updated=None, friendly_name=None, unique_name=None) -> web.Response:
    """update_channel

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: 
    :type attributes: str
    :param created_by: 
    :type created_by: str
    :param date_created: 
    :type date_created: str
    :param date_updated: 
    :type date_updated: str
    :param friendly_name: 
    :type friendly_name: str
    :param unique_name: 
    :type unique_name: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)
