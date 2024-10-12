from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_channel_sender_response import ListChannelSenderResponse
from openapi_server.models.messaging_v1_service_channel_sender import MessagingV1ServiceChannelSender
from openapi_server import util


async def fetch_channel_sender(request: web.Request, messaging_service_sid, sid) -> web.Response:
    """fetch_channel_sender

    

    :param messaging_service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.
    :type messaging_service_sid: str
    :param sid: The SID of the ChannelSender resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_channel_sender(request: web.Request, messaging_service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_channel_sender

    

    :param messaging_service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.
    :type messaging_service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
