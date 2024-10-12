from typing import List, Dict
from aiohttp import web

from openapi_server.models.events_v1_sink import EventsV1Sink
from openapi_server.models.list_sink_response import ListSinkResponse
from openapi_server.models.sink_enum_sink_type import SinkEnumSinkType
from openapi_server import util


async def create_sink(request: web.Request, description, sink_configuration, sink_type) -> web.Response:
    """create_sink

    Create a new Sink

    :param description: A human readable description for the Sink **This value should not contain PII.**
    :type description: str
    :param sink_configuration: The information required for Twilio to connect to the provided Sink encoded as JSON.
    :type sink_configuration: dict | bytes
    :param sink_type: 
    :type sink_type: str

    """
    sink_configuration = object.from_dict(sink_configuration)
    return web.Response(status=200)


async def delete_sink(request: web.Request, sid) -> web.Response:
    """delete_sink

    Delete a specific Sink.

    :param sid: A 34 character string that uniquely identifies this Sink.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sink(request: web.Request, sid) -> web.Response:
    """fetch_sink

    Fetch a specific Sink.

    :param sid: A 34 character string that uniquely identifies this Sink.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sink(request: web.Request, in_use=None, status=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sink

    Retrieve a paginated list of Sinks belonging to the account used to make the request.

    :param in_use: A boolean query parameter filtering the results to return sinks used/not used by a subscription.
    :type in_use: bool
    :param status: A String query parameter filtering the results by status &#x60;initialized&#x60;, &#x60;validating&#x60;, &#x60;active&#x60; or &#x60;failed&#x60;.
    :type status: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sink(request: web.Request, sid, description) -> web.Response:
    """update_sink

    Update a specific Sink

    :param sid: A 34 character string that uniquely identifies this Sink.
    :type sid: str
    :param description: A human readable description for the Sink **This value should not contain PII.**
    :type description: str

    """
    return web.Response(status=200)
