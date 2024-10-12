from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_interaction_interaction_channel_interaction_channel_invite import FlexV1InteractionInteractionChannelInteractionChannelInvite
from openapi_server.models.list_interaction_channel_invite_response import ListInteractionChannelInviteResponse
from openapi_server import util


async def create_interaction_channel_invite(request: web.Request, interaction_sid, channel_sid, routing) -> web.Response:
    """create_interaction_channel_invite

    Invite an Agent or a TaskQueue to a Channel.

    :param interaction_sid: The Interaction SID for this Channel.
    :type interaction_sid: str
    :param channel_sid: The Channel SID for this Invite.
    :type channel_sid: str
    :param routing: The Interaction&#39;s routing logic.
    :type routing: dict | bytes

    """
    routing = object.from_dict(routing)
    return web.Response(status=200)


async def list_interaction_channel_invite(request: web.Request, interaction_sid, channel_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_interaction_channel_invite

    List all Invites for a Channel.

    :param interaction_sid: The Interaction SID for this Channel.
    :type interaction_sid: str
    :param channel_sid: The Channel SID for this Participant.
    :type channel_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
