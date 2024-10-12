from typing import List, Dict
from aiohttp import web

from openapi_server.models.personal_snippet import PersonalSnippet
from openapi_server.models.post_v3_snippets_request import PostV3SnippetsRequest
from openapi_server.models.put_v3_snippets_id_request import PutV3SnippetsIdRequest
from openapi_server import util


async def delete_v3_snippets_id(request: web.Request, id) -> web.Response:
    """Remove snippet

    This feature was introduced in GitLab 8.15.

    :param id: The ID of a snippet
    :type id: int

    """
    return web.Response(status=200)


async def get_v3_snippets(request: web.Request, page=None, per_page=None) -> web.Response:
    """Get a snippets list for authenticated user

    This feature was introduced in GitLab 8.15.

    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_snippets_id(request: web.Request, id) -> web.Response:
    """Get a single snippet

    This feature was introduced in GitLab 8.15.

    :param id: The ID of a snippet
    :type id: int

    """
    return web.Response(status=200)


async def get_v3_snippets_id_raw(request: web.Request, id) -> web.Response:
    """Get a raw snippet

    This feature was introduced in GitLab 8.15.

    :param id: The ID of a snippet
    :type id: int

    """
    return web.Response(status=200)


async def get_v3_snippets_public(request: web.Request, page=None, per_page=None) -> web.Response:
    """List all public snippets current_user has access to

    This feature was introduced in GitLab 8.15.

    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def post_v3_snippets(request: web.Request, body) -> web.Response:
    """Create new snippet

    This feature was introduced in GitLab 8.15.

    :param body: 
    :type body: dict | bytes

    """
    body = PostV3SnippetsRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_snippets_id(request: web.Request, id, body=None) -> web.Response:
    """Update an existing snippet

    This feature was introduced in GitLab 8.15.

    :param id: The ID of a snippet
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3SnippetsIdRequest.from_dict(body)
    return web.Response(status=200)
