from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_alpha_sender_response import ListAlphaSenderResponse
from openapi_server.models.messaging_v1_service_alpha_sender import MessagingV1ServiceAlphaSender
from openapi_server import util


async def create_alpha_sender(request: web.Request, service_sid, alpha_sender) -> web.Response:
    """create_alpha_sender

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the resource under.
    :type service_sid: str
    :param alpha_sender: The Alphanumeric Sender ID string. Can be up to 11 characters long. Valid characters are A-Z, a-z, 0-9, space, hyphen &#x60;-&#x60;, plus &#x60;+&#x60;, underscore &#x60;_&#x60; and ampersand &#x60;&amp;&#x60;. This value cannot contain only numbers.
    :type alpha_sender: str

    """
    return web.Response(status=200)


async def delete_alpha_sender(request: web.Request, service_sid, sid) -> web.Response:
    """delete_alpha_sender

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.
    :type service_sid: str
    :param sid: The SID of the AlphaSender resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_alpha_sender(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_alpha_sender

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.
    :type service_sid: str
    :param sid: The SID of the AlphaSender resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_alpha_sender(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_alpha_sender

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
