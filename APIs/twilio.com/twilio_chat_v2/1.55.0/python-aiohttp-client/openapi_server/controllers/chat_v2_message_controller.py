from typing import List, Dict
from aiohttp import web

from openapi_server.models.chat_v2_service_channel_message import ChatV2ServiceChannelMessage
from openapi_server.models.list_message_response import ListMessageResponse
from openapi_server.models.message_enum_order_type import MessageEnumOrderType
from openapi_server.models.message_enum_webhook_enabled_type import MessageEnumWebhookEnabledType
from openapi_server import util


async def create_message(request: web.Request, service_sid, channel_sid, x_twilio_webhook_enabled=None, attributes=None, body=None, date_created=None, date_updated=None, _from=None, last_updated_by=None, media_sid=None) -> web.Response:
    """create_message

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Message resource under.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Message resource belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: A valid JSON string that contains application-specific data.
    :type attributes: str
    :param body: The message to send to the channel. Can be an empty string or &#x60;null&#x60;, which sets the value as an empty string. You can send structured data in the body by serializing it as a string.
    :type body: str
    :param date_created: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat&#39;s history is being recreated from a backup/separate source.
    :type date_created: str
    :param date_updated: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
    :type date_updated: str
    :param _from: The [Identity](https://www.twilio.com/docs/chat/identity) of the new message&#39;s author. The default value is &#x60;system&#x60;.
    :type _from: str
    :param last_updated_by: The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable.
    :type last_updated_by: str
    :param media_sid: The SID of the [Media](https://www.twilio.com/docs/chat/rest/media) to attach to the new Message.
    :type media_sid: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def delete_message(request: web.Request, service_sid, channel_sid, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_message

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the Message resource from.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to delete belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param sid: The SID of the Message resource to delete.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

    """
    return web.Response(status=200)


async def fetch_message(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """fetch_message

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Message resource from.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to fetch belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param sid: The SID of the Message resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_message(request: web.Request, service_sid, channel_sid, order=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_message

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Message resources from.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to read belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param order: The sort order of the returned messages. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) with &#x60;asc&#x60; as the default.
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

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Message resource in.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to update belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param sid: The SID of the Message resource to update.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: A valid JSON string that contains application-specific data.
    :type attributes: str
    :param body: The message to send to the channel. Can be an empty string or &#x60;null&#x60;, which sets the value as an empty string. You can send structured data in the body by serializing it as a string.
    :type body: str
    :param date_created: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat&#39;s history is being recreated from a backup/separate source.
    :type date_created: str
    :param date_updated: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
    :type date_updated: str
    :param _from: The [Identity](https://www.twilio.com/docs/chat/identity) of the message&#39;s author.
    :type _from: str
    :param last_updated_by: The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable.
    :type last_updated_by: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)
