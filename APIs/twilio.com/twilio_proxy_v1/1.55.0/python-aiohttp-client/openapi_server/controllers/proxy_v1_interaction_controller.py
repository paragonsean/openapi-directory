from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_interaction_response import ListInteractionResponse
from openapi_server.models.proxy_v1_service_session_interaction import ProxyV1ServiceSessionInteraction
from openapi_server import util


async def delete_interaction(request: web.Request, service_sid, session_sid, sid) -> web.Response:
    """delete_interaction

    Delete a specific Interaction.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to delete.
    :type service_sid: str
    :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to delete.
    :type session_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Interaction resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_interaction(request: web.Request, service_sid, session_sid, sid) -> web.Response:
    """fetch_interaction

    Retrieve a list of Interactions for a given [Session](https://www.twilio.com/docs/proxy/api/session).

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
    :type service_sid: str
    :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch.
    :type session_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Interaction resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_interaction(request: web.Request, service_sid, session_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_interaction

    Retrieve a list of all Interactions for a Session. A maximum of 100 records will be returned per page.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from.
    :type service_sid: str
    :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) to read the resources from.
    :type session_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
