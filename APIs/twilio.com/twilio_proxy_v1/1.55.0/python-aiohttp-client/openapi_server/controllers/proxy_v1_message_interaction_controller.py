from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_message_interaction_response import ListMessageInteractionResponse
from openapi_server.models.proxy_v1_service_session_participant_message_interaction import ProxyV1ServiceSessionParticipantMessageInteraction
from openapi_server import util


async def create_message_interaction(request: web.Request, service_sid, session_sid, participant_sid, body=None, media_url=None) -> web.Response:
    """create_message_interaction

    Create a new message Interaction to send directly from your system to one [Participant](https://www.twilio.com/docs/proxy/api/participant).  The &#x60;inbound&#x60; properties for the Interaction will always be empty.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
    :type service_sid: str
    :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource.
    :type session_sid: str
    :param participant_sid: The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) resource.
    :type participant_sid: str
    :param body: The message to send to the participant
    :type body: str
    :param media_url: Reserved. Not currently supported.
    :type media_url: List[str]

    """
    return web.Response(status=200)


async def fetch_message_interaction(request: web.Request, service_sid, session_sid, participant_sid, sid) -> web.Response:
    """fetch_message_interaction

    

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
    :type service_sid: str
    :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch.
    :type session_sid: str
    :param participant_sid: The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) resource.
    :type participant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the MessageInteraction resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_message_interaction(request: web.Request, service_sid, session_sid, participant_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_message_interaction

    

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from.
    :type service_sid: str
    :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) to read the resources from.
    :type session_sid: str
    :param participant_sid: The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) to read the resources from.
    :type participant_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
