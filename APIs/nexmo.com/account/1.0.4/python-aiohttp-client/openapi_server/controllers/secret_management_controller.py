from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_api_secret400_response import CreateAPISecret400Response
from openapi_server.models.create_secret_request import CreateSecretRequest
from openapi_server.models.error_api_key_not_found import ErrorAPIKeyNotFound
from openapi_server.models.retrieve_api_secret404_response import RetrieveAPISecret404Response
from openapi_server.models.retrieve_api_secrets200_response import RetrieveAPISecrets200Response
from openapi_server.models.retrieve_api_secrets401_response import RetrieveAPISecrets401Response
from openapi_server.models.revoke_api_secret403_response import RevokeAPISecret403Response
from openapi_server.models.secret_info import SecretInfo
from openapi_server import util


async def create_api_secret(request: web.Request, api_key, body) -> web.Response:
    """Create API Secret

    

    :param api_key: The API key to manage secrets for
    :type api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateSecretRequest.from_dict(body)
    return web.Response(status=200)


async def retrieve_api_secret(request: web.Request, api_key, secret_id) -> web.Response:
    """Retrieve one API Secret

    

    :param api_key: The API key to manage secrets for
    :type api_key: str
    :param secret_id: ID of the API Secret
    :type secret_id: str

    """
    return web.Response(status=200)


async def retrieve_api_secrets(request: web.Request, api_key) -> web.Response:
    """Retrieve API Secrets

    

    :param api_key: The API key to manage secrets for
    :type api_key: str

    """
    return web.Response(status=200)


async def revoke_api_secret(request: web.Request, api_key, secret_id) -> web.Response:
    """Revoke an API Secret

    

    :param api_key: The API key to manage secrets for
    :type api_key: str
    :param secret_id: ID of the API Secret
    :type secret_id: str

    """
    return web.Response(status=200)
