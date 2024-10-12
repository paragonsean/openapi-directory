from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_dm_conversation_request import CreateDmConversationRequest
from openapi_server.models.create_dm_event_response import CreateDmEventResponse
from openapi_server.models.create_message_request import CreateMessageRequest
from openapi_server.models.error import Error
from openapi_server.models.get2_dm_conversations_id_dm_events_response import Get2DmConversationsIdDmEventsResponse
from openapi_server.models.get2_dm_conversations_with_participant_id_dm_events_response import Get2DmConversationsWithParticipantIdDmEventsResponse
from openapi_server.models.get2_dm_events_response import Get2DmEventsResponse
from openapi_server.models.problem import Problem
from openapi_server import util


async def dm_conversation_by_id_event_id_create(request: web.Request, dm_conversation_id, body=None) -> web.Response:
    """Send a new message to a DM Conversation

    Creates a new message for a DM Conversation specified by DM Conversation ID

    :param dm_conversation_id: The DM Conversation ID.
    :type dm_conversation_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateMessageRequest.from_dict(body)
    return web.Response(status=200)


async def dm_conversation_id_create(request: web.Request, body=None) -> web.Response:
    """Create a new DM Conversation

    Creates a new DM Conversation.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateDmConversationRequest.from_dict(body)
    return web.Response(status=200)


async def dm_conversation_with_user_event_id_create(request: web.Request, participant_id, body=None) -> web.Response:
    """Send a new message to a user

    Creates a new message for a DM Conversation with a participant user by ID

    :param participant_id: The ID of the recipient user that will receive the DM.
    :type participant_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateMessageRequest.from_dict(body)
    return web.Response(status=200)


async def get_dm_conversations_id_dm_events(request: web.Request, id, max_results=None, pagination_token=None, event_types=None, dm_event_fields=None, expansions=None, media_fields=None, user_fields=None, tweet_fields=None) -> web.Response:
    """Get DM Events for a DM Conversation

    Returns DM Events for a DM Conversation

    :param id: The DM Conversation ID.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param event_types: The set of event_types to include in the results.
    :type event_types: List[str]
    :param dm_event_fields: A comma separated list of DmEvent fields to display.
    :type dm_event_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def get_dm_conversations_with_participant_id_dm_events(request: web.Request, participant_id, max_results=None, pagination_token=None, event_types=None, dm_event_fields=None, expansions=None, media_fields=None, user_fields=None, tweet_fields=None) -> web.Response:
    """Get DM Events for a DM Conversation

    Returns DM Events for a DM Conversation

    :param participant_id: The ID of the participant user for the One to One DM conversation.
    :type participant_id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param event_types: The set of event_types to include in the results.
    :type event_types: List[str]
    :param dm_event_fields: A comma separated list of DmEvent fields to display.
    :type dm_event_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def get_dm_events(request: web.Request, max_results=None, pagination_token=None, event_types=None, dm_event_fields=None, expansions=None, media_fields=None, user_fields=None, tweet_fields=None) -> web.Response:
    """Get recent DM Events

    Returns recent DM Events across DM conversations

    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param event_types: The set of event_types to include in the results.
    :type event_types: List[str]
    :param dm_event_fields: A comma separated list of DmEvent fields to display.
    :type dm_event_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)
