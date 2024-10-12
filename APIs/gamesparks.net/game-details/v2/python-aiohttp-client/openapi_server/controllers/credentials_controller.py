from typing import List, Dict
from aiohttp import web

from openapi_server.models.message_model import MessageModel
from openapi_server import util


async def update_credential_secret_using_post(request: web.Request, api_key, credential_name) -> web.Response:
    """Resets the secret of a credential

    

    :param api_key: apiKey
    :type api_key: str
    :param credential_name: credentialName
    :type credential_name: str

    """
    return web.Response(status=200)
