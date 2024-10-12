from typing import List, Dict
from aiohttp import web

from openapi_server.models.execution_enum_status import ExecutionEnumStatus
from openapi_server.models.list_execution_response import ListExecutionResponse
from openapi_server.models.studio_v2_flow_execution import StudioV2FlowExecution
from openapi_server import util


async def create_execution(request: web.Request, flow_sid, _from, to, parameters=None) -> web.Response:
    """create_execution

    Triggers a new Execution for the Flow

    :param flow_sid: The SID of the Excecution&#39;s Flow.
    :type flow_sid: str
    :param _from: The Twilio phone number to send messages or initiate calls from during the Flow&#39;s Execution. Available as variable &#x60;{{flow.channel.address}}&#x60;. For SMS, this can also be a Messaging Service SID.
    :type _from: str
    :param to: The Contact phone number to start a Studio Flow Execution, available as variable &#x60;{{contact.channel.address}}&#x60;.
    :type to: str
    :param parameters: JSON data that will be added to the Flow&#39;s context and that can be accessed as variables inside your Flow. For example, if you pass in &#x60;Parameters&#x3D;{\\\&quot;name\\\&quot;:\\\&quot;Zeke\\\&quot;}&#x60;, a widget in your Flow can reference the variable &#x60;{{flow.data.name}}&#x60;, which returns \\\&quot;Zeke\\\&quot;. Note: the JSON value must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you may need to add quotes or URL encode the JSON string.
    :type parameters: dict | bytes

    """
    parameters = object.from_dict(parameters)
    return web.Response(status=200)


async def delete_execution(request: web.Request, flow_sid, sid) -> web.Response:
    """delete_execution

    Delete the Execution and all Steps relating to it.

    :param flow_sid: The SID of the Flow with the Execution resources to delete.
    :type flow_sid: str
    :param sid: The SID of the Execution resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_execution(request: web.Request, flow_sid, sid) -> web.Response:
    """fetch_execution

    Retrieve an Execution

    :param flow_sid: The SID of the Flow with the Execution resource to fetch
    :type flow_sid: str
    :param sid: The SID of the Execution resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_execution(request: web.Request, flow_sid, date_created_from=None, date_created_to=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_execution

    Retrieve a list of all Executions for the Flow.

    :param flow_sid: The SID of the Flow with the Execution resources to read.
    :type flow_sid: str
    :param date_created_from: Only show Execution resources starting on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as &#x60;YYYY-MM-DDThh:mm:ss-hh:mm&#x60;.
    :type date_created_from: str
    :param date_created_to: Only show Execution resources starting before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as &#x60;YYYY-MM-DDThh:mm:ss-hh:mm&#x60;.
    :type date_created_to: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    date_created_from = util.deserialize_datetime(date_created_from)
    date_created_to = util.deserialize_datetime(date_created_to)
    return web.Response(status=200)


async def update_execution(request: web.Request, flow_sid, sid, status) -> web.Response:
    """update_execution

    Update the status of an Execution to &#x60;ended&#x60;.

    :param flow_sid: The SID of the Flow with the Execution resources to update.
    :type flow_sid: str
    :param sid: The SID of the Execution resource to update.
    :type sid: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)
