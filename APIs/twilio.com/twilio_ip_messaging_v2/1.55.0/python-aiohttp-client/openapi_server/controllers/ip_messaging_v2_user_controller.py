from typing import List, Dict
from aiohttp import web

from openapi_server.models.ip_messaging_v2_service_user import IpMessagingV2ServiceUser
from openapi_server.models.list_user_response import ListUserResponse
from openapi_server.models.user_enum_webhook_enabled_type import UserEnumWebhookEnabledType
from openapi_server import util


async def create_user(request: web.Request, service_sid, identity, x_twilio_webhook_enabled=None, attributes=None, friendly_name=None, role_sid=None) -> web.Response:
    """create_user

    

    :param service_sid: 
    :type service_sid: str
    :param identity: 
    :type identity: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: 
    :type attributes: str
    :param friendly_name: 
    :type friendly_name: str
    :param role_sid: 
    :type role_sid: str

    """
    return web.Response(status=200)


async def delete_user(request: web.Request, service_sid, sid) -> web.Response:
    """delete_user

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_user(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_user

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_user(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_user

    

    :param service_sid: 
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_user(request: web.Request, service_sid, sid, x_twilio_webhook_enabled=None, attributes=None, friendly_name=None, role_sid=None) -> web.Response:
    """update_user

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: 
    :type attributes: str
    :param friendly_name: 
    :type friendly_name: str
    :param role_sid: 
    :type role_sid: str

    """
    return web.Response(status=200)
