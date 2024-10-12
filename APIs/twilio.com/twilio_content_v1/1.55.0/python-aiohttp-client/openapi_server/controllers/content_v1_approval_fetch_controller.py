from typing import List, Dict
from aiohttp import web

from openapi_server.models.content_v1_content_approval_fetch import ContentV1ContentApprovalFetch
from openapi_server import util


async def fetch_approval_fetch(request: web.Request, sid) -> web.Response:
    """fetch_approval_fetch

    Fetch a Content resource&#39;s approval status by its unique Content Sid

    :param sid: The Twilio-provided string that uniquely identifies the Content resource whose approval information to fetch.
    :type sid: str

    """
    return web.Response(status=200)
