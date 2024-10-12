from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_user_channel_response import ListUserChannelResponse
from openapi_server import util


async def list_user_channel(request: web.Request, service_sid, user_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_user_channel

    List all Channels for a given User.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
    :type service_sid: str
    :param user_sid: The SID of the [User](https://www.twilio.com/docs/api/chat/rest/users) to read the User Channel resources from.
    :type user_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
