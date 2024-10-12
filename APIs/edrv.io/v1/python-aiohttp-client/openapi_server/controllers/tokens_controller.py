from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_drivers200_response import GetDrivers200Response
from openapi_server.models.patch_token_request import PatchTokenRequest
from openapi_server.models.post_tokens_request import PostTokensRequest
from openapi_server import util


async def delete_token(request: web.Request, id) -> web.Response:
    """delete_token

    Use to delete a token

    :param id: The token id that needs to be deleted
    :type id: str

    """
    return web.Response(status=200)


async def get_token(request: web.Request, id, include_driver=None, include_organization=None) -> web.Response:
    """get_token

    Get a single token&#39;s data

    :param id: The token id that needs to be fetched
    :type id: str
    :param include_driver: Populate driver
    :type include_driver: bool
    :param include_organization: Populate organization
    :type include_organization: bool

    """
    return web.Response(status=200)


async def get_tokens(request: web.Request, paginate_limit=None, paginate_page=None, paginate_enabled=None, sort_by=None, sort_order=None, created_at_gte=None, created_at_lte=None, updated_at_gte=None, updated_at_lte=None, include_driver=None, include_organization=None) -> web.Response:
    """get_tokens

    List tokens

    :param paginate_limit: Number of results per page
    :type paginate_limit: int
    :param paginate_page: The queried page index
    :type paginate_page: str
    :param paginate_enabled: Enable pagination
    :type paginate_enabled: bool
    :param sort_by: Sort data by this key
    :type sort_by: str
    :param sort_order: asc to sort ascending (default is desc - descending)
    :type sort_order: str
    :param created_at_gte: Date as ISO String
    :type created_at_gte: str
    :param created_at_lte: Date as ISO String
    :type created_at_lte: str
    :param updated_at_gte: Date as ISO String
    :type updated_at_gte: str
    :param updated_at_lte: Date as ISO String
    :type updated_at_lte: str
    :param include_driver: Populate driver
    :type include_driver: bool
    :param include_organization: Populate organization
    :type include_organization: bool

    """
    created_at_gte = util.deserialize_datetime(created_at_gte)
    created_at_lte = util.deserialize_datetime(created_at_lte)
    updated_at_gte = util.deserialize_datetime(updated_at_gte)
    updated_at_lte = util.deserialize_datetime(updated_at_lte)
    return web.Response(status=200)


async def patch_token(request: web.Request, id, body) -> web.Response:
    """patch_token

    Update a token

    :param id: ID of token that needs to be updated
    :type id: str
    :param body: Include token properties to create here
    :type body: dict | bytes

    """
    body = PatchTokenRequest.from_dict(body)
    return web.Response(status=200)


async def post_tokens(request: web.Request, body) -> web.Response:
    """post_tokens

    Create a new token

    :param body: Include token properties to create here
    :type body: dict | bytes

    """
    body = PostTokensRequest.from_dict(body)
    return web.Response(status=200)
