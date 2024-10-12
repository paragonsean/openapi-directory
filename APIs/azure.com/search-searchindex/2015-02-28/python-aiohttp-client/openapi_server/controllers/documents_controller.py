from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def documents_count(request: web.Request, api_version, client_request_id=None) -> web.Response:
    """documents_count

    Queries the number of documents in the Azure Search index.

    :param api_version: Client Api Version.
    :type api_version: str
    :param client_request_id: Tracking ID sent with the request to help with debugging.
    :type client_request_id: str
    :type client_request_id: str

    """
    return web.Response(status=200)
