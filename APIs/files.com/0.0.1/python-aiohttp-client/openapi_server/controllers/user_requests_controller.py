from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_request_entity import UserRequestEntity
from openapi_server import util


async def delete_user_requests_id(request: web.Request, id) -> web.Response:
    """Delete User Request

    Delete User Request

    :param id: User Request ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_user_requests(request: web.Request, cursor=None, per_page=None) -> web.Response:
    """List User Requests

    List User Requests

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_user_requests_id(request: web.Request, id) -> web.Response:
    """Show User Request

    Show User Request

    :param id: User Request ID.
    :type id: int

    """
    return web.Response(status=200)


async def post_user_requests(request: web.Request, details, email, name) -> web.Response:
    """Create User Request

    Create User Request

    :param details: Details of the user request
    :type details: str
    :param email: Email of user requested
    :type email: str
    :param name: Name of user requested
    :type name: str

    """
    return web.Response(status=200)
