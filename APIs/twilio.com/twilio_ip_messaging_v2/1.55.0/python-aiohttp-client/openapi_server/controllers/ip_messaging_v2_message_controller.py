from typing import List, Dict
from aiohttp import web

from openapi_server.models.ip_messaging_v2_service_channel_message import IpMessagingV2ServiceChannelMessage
from openapi_server.models.list_message_response import ListMessageResponse
from openapi_server.models.message_enum_order_type import MessageEnumOrderType
from openapi_server.models.message_enum_webhook_enabled_type import MessageEnumWebhookEnabledType
from openapi_server import util


async def create_message(request: web.Request, service_sid, channel_sid, x_twilio_webhook_enabled=None, attributes=None, body=None, date_created=None, date_updated=None, _from=None, last_updated_by=None, media_sid=None) -> web.Response:
    """create_message

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: 
    :type attributes: str
    :param body: 
    :type body: str
    :param date_created: 
    :type date_created: str
    :param date_updated: 
    :type date_updated: str
    :param _from: 
    :type _from: str
    :param last_updated_by: 
    :type last_updated_by: str
    :param media_sid: 
    :type media_sid: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def delete_message(request: web.Request, service_sid, channel_sid, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_message

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param sid: 
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

    """
    return web.Response(status=200)


async def fetch_message(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """fetch_message

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_message(request: web.Request, service_sid, channel_sid, order=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_message

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param order: 
    :type order: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_message(request: web.Request, service_sid, channel_sid, sid, x_twilio_webhook_enabled=None, attributes=None, body=None, date_created=None, date_updated=None, _from=None, last_updated_by=None) -> web.Response:
    """update_message

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param sid: 
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: 
    :type attributes: str
    :param body: 
    :type body: str
    :param date_created: 
    :type date_created: str
    :param date_updated: 
    :type date_updated: str
    :param _from: 
    :type _from: str
    :param last_updated_by: 
    :type last_updated_by: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)
