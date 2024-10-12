from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_engagement_response import ListEngagementResponse
from openapi_server.models.studio_v1_flow_engagement import StudioV1FlowEngagement
from openapi_server import util


async def create_engagement(request: web.Request, flow_sid, _from, to, parameters=None) -> web.Response:
    """create_engagement

    Triggers a new Engagement for the Flow

    :param flow_sid: The SID of the Flow.
    :type flow_sid: str
    :param _from: The Twilio phone number to send messages or initiate calls from during the Flow Engagement. Available as variable &#x60;{{flow.channel.address}}&#x60;
    :type _from: str
    :param to: The Contact phone number to start a Studio Flow Engagement, available as variable &#x60;{{contact.channel.address}}&#x60;.
    :type to: str
    :param parameters: A JSON string we will add to your flow&#39;s context and that you can access as variables inside your flow. For example, if you pass in &#x60;Parameters&#x3D;{&#39;name&#39;:&#39;Zeke&#39;}&#x60; then inside a widget you can reference the variable &#x60;{{flow.data.name}}&#x60; which will return the string &#39;Zeke&#39;. Note: the JSON value must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you may need to add quotes or URL encode your JSON string.
    :type parameters: dict | bytes

    """
    parameters = object.from_dict(parameters)
    return web.Response(status=200)


async def delete_engagement(request: web.Request, flow_sid, sid) -> web.Response:
    """delete_engagement

    Delete this Engagement and all Steps relating to it.

    :param flow_sid: The SID of the Flow to delete Engagements from.
    :type flow_sid: str
    :param sid: The SID of the Engagement resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_engagement(request: web.Request, flow_sid, sid) -> web.Response:
    """fetch_engagement

    Retrieve an Engagement

    :param flow_sid: The SID of the Flow.
    :type flow_sid: str
    :param sid: The SID of the Engagement resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_engagement(request: web.Request, flow_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_engagement

    Retrieve a list of all Engagements for the Flow.

    :param flow_sid: The SID of the Flow to read Engagements from.
    :type flow_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
