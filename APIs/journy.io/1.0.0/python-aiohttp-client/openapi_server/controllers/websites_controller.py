from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.get_tracking_snippet200_response import GetTrackingSnippet200Response
from openapi_server import util


async def get_tracking_snippet(request: web.Request, domain) -> web.Response:
    """Get snippet for a website

    Endpoint used to get a snippet for a website.

    :param domain: The domain you want to receive a snippet for
    :type domain: str

    """
    return web.Response(status=200)
