from typing import List, Dict
from aiohttp import web

from openapi_server.models.chat_v1_service_channel_message import ChatV1ServiceChannelMessage
from openapi_server.models.list_message_response import ListMessageResponse
from openapi_server.models.message_enum_order_type import MessageEnumOrderType
from openapi_server import util


async def create_message(request: web.Request, service_sid, channel_sid, body, attributes=None, _from=None) -> web.Response:
    """create_message

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to create the resource under.
    :type service_sid: str
    :param channel_sid: The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the new resource belongs to. Can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param body: The message to send to the channel. Can also be an empty string or &#x60;null&#x60;, which sets the value as an empty string. You can send structured data in the body by serializing it as a string.
    :type body: str
    :param attributes: A valid JSON string that contains application-specific data.
    :type attributes: str
    :param _from: The [identity](https://www.twilio.com/docs/api/chat/guides/identity) of the new message&#39;s author. The default value is &#x60;system&#x60;.
    :type _from: str

    """
    return web.Response(status=200)


async def delete_message(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """delete_message

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to delete the resource from.
    :type service_sid: str
    :param channel_sid: The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the message to delete belongs to.  Can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Message resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_message(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """fetch_message

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from.
    :type service_sid: str
    :param channel_sid: The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the message to fetch belongs to. Can be the Channel&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Message resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_message(request: web.Request, service_sid, channel_sid, order=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_message

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
    :type service_sid: str
    :param channel_sid: The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the message to read belongs to. Can be the Channel&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
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


async def update_message(request: web.Request, service_sid, channel_sid, sid, attributes=None, body=None) -> web.Response:
    """update_message

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to update the resource from.
    :type service_sid: str
    :param channel_sid: The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the message belongs to. Can be the Channel&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Message resource to update.
    :type sid: str
    :param attributes: A valid JSON string that contains application-specific data.
    :type attributes: str
    :param body: The message to send to the channel. Can also be an empty string or &#x60;null&#x60;, which sets the value as an empty string. You can send structured data in the body by serializing it as a string.
    :type body: str

    """
    return web.Response(status=200)
