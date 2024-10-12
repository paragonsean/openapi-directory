from typing import List, Dict
from aiohttp import web

from openapi_server.models.mime_email_payload import MimeEmailPayload
from openapi_server import util


async def v2_mime_email_payloads_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch the MIME content for email

    Fetch the MIME content for email. 

    :param id: ID of Email
    :type id: str

    """
    return web.Response(status=200)
