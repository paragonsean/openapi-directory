from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.create_access_token_request import CreateAccessTokenRequest
from openapi_server.models.error import Error
from openapi_server.models.get_access_tokens_response import GetAccessTokensResponse
from openapi_server.models.patch_access_token_request import PatchAccessTokenRequest
from openapi_server.models.v2_access_tokens_uuid_get200_response import V2AccessTokensUuidGet200Response
from openapi_server.models.value_error import ValueError
from openapi_server import util


async def v2_access_tokens_get(request: web.Request, page=None, page_size=None) -> web.Response:
    """Get a list of personal access tokens

    Returns a paginated list of personal access tokens.

    :param page: 
    :type page: 
    :param page_size: 
    :type page_size: 

    """
    return web.Response(status=200)


async def v2_access_tokens_post(request: web.Request, body) -> web.Response:
    """Create a personal access token

    Creates and returns a personal access token.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAccessTokenRequest.from_dict(body)
    return web.Response(status=200)


async def v2_access_tokens_uuid_delete(request: web.Request, uuid) -> web.Response:
    """Delete a personal access token

    Deletes a personal access token permanently. This cannot be undone. 

    :param uuid: 
    :type uuid: str

    """
    return web.Response(status=200)


async def v2_access_tokens_uuid_get(request: web.Request, uuid) -> web.Response:
    """Get a personal access token

    Returns a personal access token by UUID.

    :param uuid: 
    :type uuid: str

    """
    return web.Response(status=200)


async def v2_access_tokens_uuid_patch(request: web.Request, uuid, body) -> web.Response:
    """Update a personal access token

    Updates a personal access token partially. You can either update the token&#39;s label or enable/disable it. 

    :param uuid: 
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchAccessTokenRequest.from_dict(body)
    return web.Response(status=200)
