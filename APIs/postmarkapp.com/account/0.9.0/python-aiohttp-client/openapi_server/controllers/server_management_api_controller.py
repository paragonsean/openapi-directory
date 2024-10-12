from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_server_payload import CreateServerPayload
from openapi_server.models.edit_server_payload import EditServerPayload
from openapi_server.models.extended_server_info import ExtendedServerInfo
from openapi_server.models.server_listing_response import ServerListingResponse
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server import util


async def create_server(request: web.Request, x_postmark_account_token, body=None) -> web.Response:
    """Create a Server

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateServerPayload.from_dict(body)
    return web.Response(status=200)


async def delete_server(request: web.Request, x_postmark_account_token, serverid) -> web.Response:
    """Delete a Server

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param serverid: The ID of the Server that should be deleted.
    :type serverid: int

    """
    return web.Response(status=200)


async def edit_server_information(request: web.Request, x_postmark_account_token, serverid, body=None) -> web.Response:
    """Edit a Server

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param serverid: The ID of the Server to update.
    :type serverid: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditServerPayload.from_dict(body)
    return web.Response(status=200)


async def get_server_information(request: web.Request, x_postmark_account_token, serverid) -> web.Response:
    """Get a Server

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param serverid: The ID of the Server to get.
    :type serverid: int

    """
    return web.Response(status=200)


async def list_servers(request: web.Request, x_postmark_account_token, count, offset, name=None) -> web.Response:
    """List servers

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param count: Number of servers to return per request.
    :type count: int
    :param offset: Number of servers to skip.
    :type offset: int
    :param name: Filter by a specific server name
    :type name: str

    """
    return web.Response(status=200)
