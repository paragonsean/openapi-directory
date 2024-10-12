from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_participant_response import ListParticipantResponse
from openapi_server.models.proxy_v1_service_session_participant import ProxyV1ServiceSessionParticipant
from openapi_server import util


async def create_participant(request: web.Request, service_sid, session_sid, identifier, friendly_name=None, proxy_identifier=None, proxy_identifier_sid=None) -> web.Response:
    """create_participant

    Add a new Participant to the Session

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
    :type service_sid: str
    :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource.
    :type session_sid: str
    :param identifier: The phone number of the Participant.
    :type identifier: str
    :param friendly_name: The string that you assigned to describe the participant. This value must be 255 characters or fewer. **This value should not have PII.**
    :type friendly_name: str
    :param proxy_identifier: The proxy phone number to use for the Participant. If not specified, Proxy will select a number from the pool.
    :type proxy_identifier: str
    :param proxy_identifier_sid: The SID of the Proxy Identifier to assign to the Participant.
    :type proxy_identifier_sid: str

    """
    return web.Response(status=200)


async def delete_participant(request: web.Request, service_sid, session_sid, sid) -> web.Response:
    """delete_participant

    Delete a specific Participant. This is a soft-delete. The participant remains associated with the session and cannot be re-added. Participants are only permanently deleted when the [Session](https://www.twilio.com/docs/proxy/api/session) is deleted.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to delete.
    :type service_sid: str
    :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to delete.
    :type session_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Participant resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_participant(request: web.Request, service_sid, session_sid, sid) -> web.Response:
    """fetch_participant

    Fetch a specific Participant.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
    :type service_sid: str
    :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch.
    :type session_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Participant resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_participant(request: web.Request, service_sid, session_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_participant

    Retrieve a list of all Participants in a Session.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resources to read.
    :type service_sid: str
    :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resources to read.
    :type session_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
