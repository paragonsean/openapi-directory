from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def show_public_keys(request: web.Request, account, kind, identifier, x_request_id=None) -> web.Response:
    """Shows all public keys for a resource.

    Shows all public keys for a resource as newline delimited string for compatibility with the authorized_keys SSH format. Returns an empty string if the resource does not exist, to prevent attackers from determining whether a resource exists. 

    :param account: Organization account name
    :type account: str
    :param kind: Type of resource
    :type kind: str
    :param identifier: ID of the resource for which to get the information about
    :type identifier: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)
