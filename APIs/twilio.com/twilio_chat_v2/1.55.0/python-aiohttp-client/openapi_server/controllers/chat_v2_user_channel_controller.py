from typing import List, Dict
from aiohttp import web

from openapi_server.models.chat_v2_service_user_user_channel import ChatV2ServiceUserUserChannel
from openapi_server.models.list_user_channel_response import ListUserChannelResponse
from openapi_server.models.user_channel_enum_notification_level import UserChannelEnumNotificationLevel
from openapi_server.models.user_channel_enum_webhook_enabled_type import UserChannelEnumWebhookEnabledType
from openapi_server import util


async def delete_user_channel(request: web.Request, service_sid, user_sid, channel_sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_user_channel

    Removes User from selected Channel.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
    :type service_sid: str
    :param user_sid: The SID of the [User](https://www.twilio.com/docs/api/chat/rest/users) to read the User Channel resources from.
    :type user_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource belongs to.
    :type channel_sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

    """
    return web.Response(status=200)


async def fetch_user_channel(request: web.Request, service_sid, user_sid, channel_sid) -> web.Response:
    """fetch_user_channel

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the User Channel resource from.
    :type service_sid: str
    :param user_sid: The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) to fetch the User Channel resource from. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource.
    :type user_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) that has the User Channel to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the Channel to fetch.
    :type channel_sid: str

    """
    return web.Response(status=200)


async def list_user_channel(request: web.Request, service_sid, user_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_user_channel

    List all Channels for a given User.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the User Channel resources from.
    :type service_sid: str
    :param user_sid: The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) to read the User Channel resources from. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource.
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

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the User Channel resource in.
    :type service_sid: str
    :param user_sid: The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) to update the User Channel resource from. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource.
    :type user_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) with the User Channel resource to update. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param last_consumed_message_index: The index of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) in the [Channel](https://www.twilio.com/docs/chat/channels) that the Member has read.
    :type last_consumed_message_index: int
    :param last_consumption_timestamp: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) read event for the Member within the [Channel](https://www.twilio.com/docs/chat/channels).
    :type last_consumption_timestamp: str
    :param notification_level: 
    :type notification_level: str

    """
    last_consumption_timestamp = util.deserialize_datetime(last_consumption_timestamp)
    return web.Response(status=200)
