from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_participant_conversation_response import ListParticipantConversationResponse
from openapi_server.models.list_service_participant_conversation_response import ListServiceParticipantConversationResponse
from openapi_server import util


async def list_participant_conversation(request: web.Request, identity=None, address=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_participant_conversation

    Retrieve a list of all Conversations that this Participant belongs to by identity or by address. Only one parameter should be specified.

    :param identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
    :type identity: str
    :param address: A unique string identifier for the conversation participant who&#39;s not a Conversation User. This parameter could be found in messaging_binding.address field of Participant resource. It should be url-encoded.
    :type address: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def list_service_participant_conversation(request: web.Request, chat_service_sid, identity=None, address=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service_participant_conversation

    Retrieve a list of all Conversations that this Participant belongs to by identity or by address. Only one parameter should be specified.

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant Conversations resource is associated with.
    :type chat_service_sid: str
    :param identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
    :type identity: str
    :param address: A unique string identifier for the conversation participant who&#39;s not a Conversation User. This parameter could be found in messaging_binding.address field of Participant resource. It should be url-encoded.
    :type address: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
