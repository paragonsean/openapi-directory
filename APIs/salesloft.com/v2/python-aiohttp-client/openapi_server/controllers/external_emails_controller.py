from typing import List, Dict
from aiohttp import web

from openapi_server.models.external_email import ExternalEmail
from openapi_server import util


async def v2_external_emails_json_post(request: web.Request, mailbox, raw) -> web.Response:
    """Create an External Email

    Creates an external email object. 

    :param mailbox: Email address of mailbox email was sent to
    :type mailbox: str
    :param raw: Base64 encoded MIME email content
    :type raw: str

    """
    return web.Response(status=200)
