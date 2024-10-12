from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_tag_response_body import CreateTagResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.list_tags_response_body import ListTagsResponseBody
from openapi_server import util


async def create_tag(request: web.Request, tag_name) -> web.Response:
    """Create a New Tag

    Create a new Tag for customizing how you track your shipments

    :param tag_name: 
    :type tag_name: str

    """
    return web.Response(status=200)


async def delete_tag(request: web.Request, tag_name) -> web.Response:
    """Delete Tag

    Delete a tag that is no longer needed

    :param tag_name: 
    :type tag_name: str

    """
    return web.Response(status=200)


async def list_tags(request: web.Request, ) -> web.Response:
    """Get Tags

    Get a list of all tags associated with an account.


    """
    return web.Response(status=200)


async def rename_tag(request: web.Request, tag_name, new_tag_name) -> web.Response:
    """Update Tag Name

    Change a tag name while still keeping the relevant shipments attached to it

    :param tag_name: 
    :type tag_name: str
    :param new_tag_name: 
    :type new_tag_name: str

    """
    return web.Response(status=200)
