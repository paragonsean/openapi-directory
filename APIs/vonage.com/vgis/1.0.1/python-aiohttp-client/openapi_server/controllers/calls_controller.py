from typing import List, Dict
from aiohttp import web

from openapi_server.models.call import Call
from openapi_server.models.call_create import CallCreate
from openapi_server.models.call_transfer import CallTransfer
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.events_count import EventsCount
from openapi_server import util


async def call_answer(request: web.Request, id) -> web.Response:
    """Answer call (On supported devices)

    

    :param id: Unique identifier of the call
    :type id: str

    """
    return web.Response(status=200)


async def call_hold(request: web.Request, id) -> web.Response:
    """Put call on hold

    

    :param id: Unique identifier of the call
    :type id: str

    """
    return web.Response(status=200)


async def call_transfer(request: web.Request, id, body) -> web.Response:
    """Transfer call

    

    :param id: Unique identifier of the call
    :type id: str
    :param body: Call transfer parameters
    :type body: dict | bytes

    """
    body = CallTransfer.from_dict(body)
    return web.Response(status=200)


async def call_unold(request: web.Request, id) -> web.Response:
    """Unhold

    

    :param id: Unique identifier of the call
    :type id: str

    """
    return web.Response(status=200)


async def call_vm_transfer(request: web.Request, id) -> web.Response:
    """Send call to voicemail

    

    :param id: Unique identifier of the call
    :type id: str

    """
    return web.Response(status=200)


async def create_call(request: web.Request, body) -> web.Response:
    """Place a call

    

    :param body: Place call parameters
    :type body: dict | bytes

    """
    body = CallCreate.from_dict(body)
    return web.Response(status=200)


async def destroy_call(request: web.Request, id) -> web.Response:
    """End a call

    

    :param id: Unique identifier of the call
    :type id: str

    """
    return web.Response(status=200)


async def get_calls_count(request: web.Request, from_date=None, to_date=None, direction=None, states=None) -> web.Response:
    """Get calls count

    

    :param from_date: Return calls that occurred after this point in time
    :type from_date: int
    :param to_date: Return calls that occurred before this point in time
    :type to_date: int
    :param direction: Filter by call direction. For multiple criteria, seperate values by a comma.
    :type direction: str
    :param states: Filter calls by state. For multiple criteria, seperate values by a comma.
    :type states: str

    """
    return web.Response(status=200)


async def get_roles(request: web.Request, id) -> web.Response:
    """Get a call

    

    :param id: Unique identifier of the call
    :type id: str

    """
    return web.Response(status=200)


async def list_calls(request: web.Request, from_date=None, to_date=None, direction=None, states=None, offset=None, size=None, order=None, sort=None) -> web.Response:
    """List active calls

    Lists currently active calls

    :param from_date: Return calls that occurred after this point in time
    :type from_date: int
    :param to_date: Return calls that occurred before this point in time
    :type to_date: int
    :param direction: Filter by call direction. For multiple criteria, seperate values by a comma.
    :type direction: str
    :param states: Filter calls by state. For multiple criteria, seperate values by a comma.
    :type states: str
    :param offset: Page number of calls to return
    :type offset: int
    :param size: Return this amount of calls in the response
    :type size: int
    :param order: Sort in either ascending or descending order
    :type order: str
    :param sort: Sort calls by property
    :type sort: str

    """
    return web.Response(status=200)
