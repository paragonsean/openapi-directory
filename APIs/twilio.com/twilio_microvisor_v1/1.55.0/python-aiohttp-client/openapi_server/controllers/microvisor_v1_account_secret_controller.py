from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_account_secret_response import ListAccountSecretResponse
from openapi_server.models.microvisor_v1_account_secret import MicrovisorV1AccountSecret
from openapi_server import util


async def create_account_secret(request: web.Request, key, value) -> web.Response:
    """create_account_secret

    Create a secret for an Account.

    :param key: The secret key; up to 100 characters.
    :type key: str
    :param value: The secret value; up to 4096 characters.
    :type value: str

    """
    return web.Response(status=200)


async def delete_account_secret(request: web.Request, key) -> web.Response:
    """delete_account_secret

    Delete a secret for an Account.

    :param key: The secret key; up to 100 characters.
    :type key: str

    """
    return web.Response(status=200)


async def fetch_account_secret(request: web.Request, key) -> web.Response:
    """fetch_account_secret

    Retrieve a Secret for an Account.

    :param key: The secret key; up to 100 characters.
    :type key: str

    """
    return web.Response(status=200)


async def list_account_secret(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_account_secret

    Retrieve a list of all Secrets for an Account.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_account_secret(request: web.Request, key, value) -> web.Response:
    """update_account_secret

    Update a secret for an Account.

    :param key: The secret key; up to 100 characters.
    :type key: str
    :param value: The secret value; up to 4096 characters.
    :type value: str

    """
    return web.Response(status=200)
