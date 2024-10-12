from typing import List, Dict
from aiohttp import web

from openapi_server.models.site import Site
from openapi_server.models.tag import Tag
from openapi_server import util


async def create_tags(request: web.Request, body) -> web.Response:
    """Create a tag

    Create a tag

    :param body: JSON object Tag
    :type body: dict | bytes

    """
    body = Tag.from_dict(body)
    return web.Response(status=200)


async def get_sites_by_tags(request: web.Request, id, name=None, access_url=None, j_version=None, ip=None, j_update=None, published=None, error=None, nb_updates=None, up=None, fields=None, limit=None, limitstart=None, order=None) -> web.Response:
    """Find sites by tag ID

    Returns a list of sites based with a specific tag id

    :param id: ID of tag that needs to be fetched
    :type id: int
    :param name: Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type name: str
    :param access_url: Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type access_url: str
    :param j_version: Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type j_version: str
    :param ip: Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type ip: str
    :param j_update: Joomla core update
    :type j_update: int
    :param published: is published
    :type published: int
    :param error: have errors
    :type error: str
    :param nb_updates: 
    :type nb_updates: str
    :param up: is the website online
    :type up: int
    :param fields: Fields to return separate by comas: name,id
    :type fields: str
    :param limit: Number of object to return (max 100, default 25)
    :type limit: int
    :param limitstart: Start of the return (default 0)
    :type limitstart: int
    :param order: ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    :type order: str

    """
    return web.Response(status=200)


async def get_tag_by_id(request: web.Request, id, fields=None) -> web.Response:
    """Find tag by ID

    Returns a tag based on ID

    :param id: ID of tag that needs to be fetched
    :type id: int
    :param fields: Fields to return separate by comas: name,id
    :type fields: str

    """
    return web.Response(status=200)


async def tags_get(request: web.Request, name=None, type=None, fields=None, limit=None, limitstart=None, order=None) -> web.Response:
    """Get a list of tags

    Returns a list of tags

    :param name: Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type name: str
    :param type: Bootstrap color of the tag
    :type type: str
    :param fields: Fields to return separate by comas: name,id
    :type fields: str
    :param limit: Number of object to return (max 100, default 25)
    :type limit: int
    :param limitstart: Start of the return (default 0)
    :type limitstart: int
    :param order: ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    :type order: str

    """
    return web.Response(status=200)


async def tags_id_delete(request: web.Request, id) -> web.Response:
    """Delete a specific tag

    Delete a specific tag

    :param id: ID of tag that needs to be deleted
    :type id: int

    """
    return web.Response(status=200)


async def tags_metadata_get(request: web.Request, ) -> web.Response:
    """Get the list of fields

    Returns a list of fields


    """
    return web.Response(status=200)


async def update_tag(request: web.Request, id, body) -> web.Response:
    """Update a tag

    Update a tag

    :param id: ID of tag
    :type id: int
    :param body: JSON object of the updated tag
    :type body: dict | bytes

    """
    body = Tag.from_dict(body)
    return web.Response(status=200)
