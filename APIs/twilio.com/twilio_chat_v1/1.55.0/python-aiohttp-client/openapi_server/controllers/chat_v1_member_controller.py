from typing import List, Dict
from aiohttp import web

from openapi_server.models.chat_v1_service_channel_member import ChatV1ServiceChannelMember
from openapi_server.models.list_member_response import ListMemberResponse
from openapi_server import util


async def create_member(request: web.Request, service_sid, channel_sid, identity, role_sid=None) -> web.Response:
    """create_member

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to create the resource under.
    :type service_sid: str
    :param channel_sid: The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the new member belongs to. Can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param identity: The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s [User](https://www.twilio.com/docs/api/chat/rest/v1/user) within the [Service](https://www.twilio.com/docs/api/chat/rest/services). See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more details.
    :type identity: str
    :param role_sid: The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/api/services).
    :type role_sid: str

    """
    return web.Response(status=200)


async def delete_member(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """delete_member

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to delete the resource from.
    :type service_sid: str
    :param channel_sid: The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the message belongs to.  Can be the Channel&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Member resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_member(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """fetch_member

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from.
    :type service_sid: str
    :param channel_sid: The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the member to fetch belongs to. Can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60; value.
    :type channel_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Member resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_member(request: web.Request, service_sid, channel_sid, identity=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_member

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
    :type service_sid: str
    :param channel_sid: The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the members to read belong to. Can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60; value.
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


async def update_member(request: web.Request, service_sid, channel_sid, sid, last_consumed_message_index=None, role_sid=None) -> web.Response:
    """update_member

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to update the resource from.
    :type service_sid: str
    :param channel_sid: The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the member to update belongs to. Can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Member resource to update.
    :type sid: str
    :param last_consumed_message_index: The index of the last [Message](https://www.twilio.com/docs/api/chat/rest/messages) that the Member has read within the [Channel](https://www.twilio.com/docs/api/chat/rest/channels).
    :type last_consumed_message_index: int
    :param role_sid: The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/api/services).
    :type role_sid: str

    """
    return web.Response(status=200)
