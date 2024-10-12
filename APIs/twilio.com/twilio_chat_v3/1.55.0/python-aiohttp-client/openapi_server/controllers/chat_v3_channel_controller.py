from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel_enum_channel_type import ChannelEnumChannelType
from openapi_server.models.channel_enum_webhook_enabled_type import ChannelEnumWebhookEnabledType
from openapi_server.models.chat_v3_channel import ChatV3Channel
from openapi_server import util


async def update_channel(request: web.Request, service_sid, sid, x_twilio_webhook_enabled=None, messaging_service_sid=None, type=None) -> web.Response:
    """update_channel

    Update a specific Channel.

    :param service_sid: The unique SID identifier of the Service.
    :type service_sid: str
    :param sid: A 34 character string that uniquely identifies this Channel.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this channel belongs to.
    :type messaging_service_sid: str
    :param type: 
    :type type: str

    """
    return web.Response(status=200)
