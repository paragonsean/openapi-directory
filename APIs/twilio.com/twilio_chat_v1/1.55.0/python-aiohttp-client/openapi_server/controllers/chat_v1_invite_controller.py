from typing import List, Dict
from aiohttp import web

from openapi_server.models.chat_v1_service_channel_invite import ChatV1ServiceChannelInvite
from openapi_server.models.list_invite_response import ListInviteResponse
from openapi_server import util


async def create_invite(request: web.Request, service_sid, channel_sid, identity, role_sid=None) -> web.Response:
    """create_invite

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to create the resource under.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the new resource belongs to.
    :type channel_sid: str
    :param identity: The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s [User](https://www.twilio.com/docs/api/chat/rest/v1/user) within the [Service](https://www.twilio.com/docs/api/chat/rest/v1/service). See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more info.
    :type identity: str
    :param role_sid: The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to the new member.
    :type role_sid: str

    """
    return web.Response(status=200)


async def delete_invite(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """delete_invite

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to delete the resource from.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource to delete belongs to.
    :type channel_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Invite resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_invite(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """fetch_invite

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource to fetch belongs to.
    :type channel_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Invite resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_invite(request: web.Request, service_sid, channel_sid, identity=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_invite

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resources to read belong to.
    :type channel_sid: str
    :param identity: The [User](https://www.twilio.com/docs/api/chat/rest/v1/user)&#39;s &#x60;identity&#x60; value of the resources to read. See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more details.
    :type identity: List[str]
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
