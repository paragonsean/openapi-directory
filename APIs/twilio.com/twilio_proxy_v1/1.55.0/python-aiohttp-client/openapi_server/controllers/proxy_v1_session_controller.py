from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_session_response import ListSessionResponse
from openapi_server.models.proxy_v1_service_session import ProxyV1ServiceSession
from openapi_server.models.session_enum_mode import SessionEnumMode
from openapi_server.models.session_enum_status import SessionEnumStatus
from openapi_server import util


async def create_session(request: web.Request, service_sid, date_expiry=None, mode=None, participants=None, status=None, ttl=None, unique_name=None) -> web.Response:
    """create_session

    Create a new Session

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
    :type service_sid: str
    :param date_expiry: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the &#x60;ttl&#x60; value.
    :type date_expiry: str
    :param mode: 
    :type mode: str
    :param participants: The Participant objects to include in the new session.
    :type participants: List[]
    :param status: 
    :type status: str
    :param ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session&#39;s last Interaction.
    :type ttl: int
    :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
    :type unique_name: str

    """
    date_expiry = util.deserialize_datetime(date_expiry)
    return web.Response(status=200)


async def delete_session(request: web.Request, service_sid, sid) -> web.Response:
    """delete_session

    Delete a specific Session.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to delete.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Session resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_session(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_session

    Fetch a specific Session.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Session resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_session(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_session

    Retrieve a list of all Sessions for the Service. A maximum of 100 records will be returned per page.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to read.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_session(request: web.Request, service_sid, sid, date_expiry=None, status=None, ttl=None) -> web.Response:
    """update_session

    Update a specific Session.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to update.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Session resource to update.
    :type sid: str
    :param date_expiry: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the &#x60;ttl&#x60; value.
    :type date_expiry: str
    :param status: 
    :type status: str
    :param ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session&#39;s last Interaction.
    :type ttl: int

    """
    date_expiry = util.deserialize_datetime(date_expiry)
    return web.Response(status=200)
