from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_call_request import CreateCallRequest
from openapi_server.models.create_call_response import CreateCallResponse
from openapi_server.models.get_call_response import GetCallResponse
from openapi_server.models.get_calls_response import GetCallsResponse
from openapi_server.models.update_call_request import UpdateCallRequest
from openapi_server import util


async def create_call(request: web.Request, body=None) -> web.Response:
    """Create an outbound call

    Create an outbound Call

    :param body: Call Details
    :type body: dict | bytes

    """
    body = CreateCallRequest.from_dict(body)
    return web.Response(status=200)


async def get_call(request: web.Request, uuid) -> web.Response:
    """Get detail of a specific call

    Get detail of a specific call

    :param uuid: UUID of the Call
    :type uuid: str

    """
    return web.Response(status=200)


async def get_calls(request: web.Request, status=None, date_start=None, date_end=None, page_size=None, record_index=None, order=None, conversation_uuid=None) -> web.Response:
    """Get details of your calls

    Get details of your calls

    :param status: Filter by call status
    :type status: str
    :param date_start: Return the records that occurred after this point in time
    :type date_start: str
    :param date_end: Return the records that occurred before this point in time
    :type date_end: str
    :param page_size: Return this amount of records in the response
    :type page_size: int
    :param record_index: Return calls from this index in the response
    :type record_index: int
    :param order: Either ascending or  descending order.
    :type order: str
    :param conversation_uuid: Return all the records associated with a specific conversation.
    :type conversation_uuid: str
    :type conversation_uuid: str

    """
    date_start = util.deserialize_datetime(date_start)
    date_end = util.deserialize_datetime(date_end)
    return web.Response(status=200)


async def update_call(request: web.Request, uuid, body) -> web.Response:
    """Modify an in progress call

    Modify an in progress call

    :param uuid: UUID of the Call
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateCallRequest.from_dict(body)
    return web.Response(status=200)
