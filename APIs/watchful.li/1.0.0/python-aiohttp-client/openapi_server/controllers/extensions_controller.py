from typing import List, Dict
from aiohttp import web

from openapi_server.models.extension import Extension
from openapi_server import util


async def get_extensions(request: web.Request, ext_name=None, siteids=None, ext_prefix=None, version=None, v_update=None, fields=None, limit=None, limitstart=None, order=None) -> web.Response:
    """Get a list Extensions

    Returns a list Extensions

    :param ext_name: Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type ext_name: str
    :param siteids: List of sites id separated by comma
    :type siteids: str
    :param ext_prefix: Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;. technical name of the extension com_xxxx
    :type ext_prefix: str
    :param version: Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type version: str
    :param v_update: update available for this extension
    :type v_update: int
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


async def get_fields_extensions(request: web.Request, ) -> web.Response:
    """Get the list of fields

    Returns a list of fields


    """
    return web.Response(status=200)


async def ignore_extension_update(request: web.Request, id) -> web.Response:
    """Set &#39;ignore updates&#39; for a given extension / site_id

    Set &#39;ignore updates&#39; for a given extension / site_id

    :param id: ID of the extension
    :type id: int

    """
    return web.Response(status=200)


async def unignore_extension_update(request: web.Request, id) -> web.Response:
    """Remove &#39;ignore updates&#39; for a given extension

    Remove &#39;ignore updates&#39; for a given extension

    :param id: ID of the extension
    :type id: int

    """
    return web.Response(status=200)


async def update_extension(request: web.Request, id) -> web.Response:
    """Update the extension on the remote site

    Update the extension on the remote site

    :param id: ID of the extension
    :type id: int

    """
    return web.Response(status=200)
