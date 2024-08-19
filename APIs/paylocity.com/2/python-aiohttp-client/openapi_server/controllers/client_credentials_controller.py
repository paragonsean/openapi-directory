from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_client_secret import AddClientSecret
from openapi_server.models.client_credentials_response import ClientCredentialsResponse
from openapi_server.models.error import Error
from openapi_server import util


async def add_client_secret(request: web.Request, body) -> web.Response:
    """Obtain new client secret.

    Obtain new client secret for Paylocity-issued client id. See Setup section for details.

    :param body: Add Client Secret Model
    :type body: dict | bytes

    """
    body = AddClientSecret.from_dict(body)
    return web.Response(status=200)
