from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_interaction_interaction_channel import FlexV1InteractionInteractionChannel
from openapi_server.models.interaction_channel_enum_update_channel_status import InteractionChannelEnumUpdateChannelStatus
from openapi_server.models.list_interaction_channel_response import ListInteractionChannelResponse
from openapi_server import util


async def fetch_interaction_channel(request: web.Request, interaction_sid, sid) -> web.Response:
    """fetch_interaction_channel

    Fetch a Channel for an Interaction.

    :param interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
    :type interaction_sid: str
    :param sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
    :type sid: str

    """
    return web.Response(status=200)


async def list_interaction_channel(request: web.Request, interaction_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_interaction_channel

    List all Channels for an Interaction.

    :param interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
    :type interaction_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_interaction_channel(request: web.Request, interaction_sid, sid, status, routing=None) -> web.Response:
    """update_interaction_channel

    Update an existing Interaction Channel.

    :param interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
    :type interaction_sid: str
    :param sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
    :type sid: str
    :param status: 
    :type status: str
    :param routing: It changes the state of associated tasks. Routing status is required, When the channel status is set to &#x60;inactive&#x60;. Allowed Value for routing status is &#x60;closed&#x60;. Otherwise Optional, if not specified, all tasks will be set to &#x60;wrapping&#x60;.
    :type routing: dict | bytes

    """
    routing = object.from_dict(routing)
    return web.Response(status=200)
