from typing import List, Dict
from aiohttp import web

from openapi_server.models.model200_ok import Model200OK
from openapi_server.models.model401_unauthorized import Model401Unauthorized
from openapi_server import util


async def create_dkim(request: web.Request, email_provider) -> web.Response:
    """Generate DKIM keys

    Create DKIM keys for sender that was setup in VTEX mail servers

    :param email_provider: E-mail address for sender that was setup in VTEX mail servers
    :type email_provider: str

    """
    return web.Response(status=200)
