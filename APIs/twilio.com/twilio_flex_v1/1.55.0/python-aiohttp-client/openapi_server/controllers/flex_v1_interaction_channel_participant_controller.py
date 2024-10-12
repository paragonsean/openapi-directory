from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_interaction_interaction_channel_interaction_channel_participant import FlexV1InteractionInteractionChannelInteractionChannelParticipant
from openapi_server.models.interaction_channel_participant_enum_status import InteractionChannelParticipantEnumStatus
from openapi_server.models.interaction_channel_participant_enum_type import InteractionChannelParticipantEnumType
from openapi_server.models.list_interaction_channel_participant_response import ListInteractionChannelParticipantResponse
from openapi_server import util


async def create_interaction_channel_participant(request: web.Request, interaction_sid, channel_sid, media_properties, type, routing_properties=None) -> web.Response:
    """create_interaction_channel_participant

    Add a Participant to a Channel.

    :param interaction_sid: The Interaction Sid for the new Channel Participant.
    :type interaction_sid: str
    :param channel_sid: The Channel Sid for the new Channel Participant.
    :type channel_sid: str
    :param media_properties: JSON representing the Media Properties for the new Participant.
    :type media_properties: dict | bytes
    :param type: 
    :type type: str
    :param routing_properties: Object representing the Routing Properties for the new Participant.
    :type routing_properties: dict | bytes

    """
    media_properties = object.from_dict(media_properties)
    routing_properties = object.from_dict(routing_properties)
    return web.Response(status=200)


async def list_interaction_channel_participant(request: web.Request, interaction_sid, channel_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_interaction_channel_participant

    List all Participants for a Channel.

    :param interaction_sid: The Interaction Sid for this channel.
    :type interaction_sid: str
    :param channel_sid: The Channel Sid for this Participant.
    :type channel_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_interaction_channel_participant(request: web.Request, interaction_sid, channel_sid, sid, status) -> web.Response:
    """update_interaction_channel_participant

    Update an existing Channel Participant.

    :param interaction_sid: The Interaction Sid for this channel.
    :type interaction_sid: str
    :param channel_sid: The Channel Sid for this Participant.
    :type channel_sid: str
    :param sid: The unique string created by Twilio to identify an Interaction Channel resource.
    :type sid: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)
