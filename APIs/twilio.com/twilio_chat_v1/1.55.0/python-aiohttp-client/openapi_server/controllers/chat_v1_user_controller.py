from typing import List, Dict
from aiohttp import web

from openapi_server.models.chat_v1_service_user import ChatV1ServiceUser
from openapi_server.models.list_user_response import ListUserResponse
from openapi_server import util


async def create_user(request: web.Request, service_sid, identity, attributes=None, friendly_name=None, role_sid=None) -> web.Response:
    """create_user

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to create the resource under.
    :type service_sid: str
    :param identity: The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s [User](https://www.twilio.com/docs/api/chat/rest/v1/user) within the [Service](https://www.twilio.com/docs/api/chat/rest/v1/service). This value is often a username or email address. See the Identity documentation for more details.
    :type identity: str
    :param attributes: A valid JSON string that contains application-specific data.
    :type attributes: str
    :param friendly_name: A descriptive string that you create to describe the new resource. This value is often used for display purposes.
    :type friendly_name: str
    :param role_sid: The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to the new User.
    :type role_sid: str

    """
    return web.Response(status=200)


async def delete_user(request: web.Request, service_sid, sid) -> web.Response:
    """delete_user

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to delete the resource from.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the User resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_user(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_user

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the User resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_user(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_user

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_user(request: web.Request, service_sid, sid, attributes=None, friendly_name=None, role_sid=None) -> web.Response:
    """update_user

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to update the resource from.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the User resource to update.
    :type sid: str
    :param attributes: A valid JSON string that contains application-specific data.
    :type attributes: str
    :param friendly_name: A descriptive string that you create to describe the resource. It is often used for display purposes.
    :type friendly_name: str
    :param role_sid: The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to this user.
    :type role_sid: str

    """
    return web.Response(status=200)
