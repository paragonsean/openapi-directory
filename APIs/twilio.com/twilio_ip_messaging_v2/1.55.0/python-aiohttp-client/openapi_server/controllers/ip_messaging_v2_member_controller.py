from typing import List, Dict
from aiohttp import web

from openapi_server.models.ip_messaging_v2_service_channel_member import IpMessagingV2ServiceChannelMember
from openapi_server.models.list_member_response import ListMemberResponse
from openapi_server.models.member_enum_webhook_enabled_type import MemberEnumWebhookEnabledType
from openapi_server import util


async def create_member(request: web.Request, service_sid, channel_sid, identity, x_twilio_webhook_enabled=None, attributes=None, date_created=None, date_updated=None, last_consumed_message_index=None, last_consumption_timestamp=None, role_sid=None) -> web.Response:
    """create_member

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param identity: 
    :type identity: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: 
    :type attributes: str
    :param date_created: 
    :type date_created: str
    :param date_updated: 
    :type date_updated: str
    :param last_consumed_message_index: 
    :type last_consumed_message_index: int
    :param last_consumption_timestamp: 
    :type last_consumption_timestamp: str
    :param role_sid: 
    :type role_sid: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    last_consumption_timestamp = util.deserialize_datetime(last_consumption_timestamp)
    return web.Response(status=200)


async def delete_member(request: web.Request, service_sid, channel_sid, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_member

    

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


async def fetch_member(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """fetch_member

    

    :param service_sid: 
    :type service_sid: str
    :param channel_sid: 
    :type channel_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_member(request: web.Request, service_sid, channel_sid, identity=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_member

    

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


async def update_member(request: web.Request, service_sid, channel_sid, sid, x_twilio_webhook_enabled=None, attributes=None, date_created=None, date_updated=None, last_consumed_message_index=None, last_consumption_timestamp=None, role_sid=None) -> web.Response:
    """update_member

    

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
    :param date_created: 
    :type date_created: str
    :param date_updated: 
    :type date_updated: str
    :param last_consumed_message_index: 
    :type last_consumed_message_index: int
    :param last_consumption_timestamp: 
    :type last_consumption_timestamp: str
    :param role_sid: 
    :type role_sid: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    last_consumption_timestamp = util.deserialize_datetime(last_consumption_timestamp)
    return web.Response(status=200)
