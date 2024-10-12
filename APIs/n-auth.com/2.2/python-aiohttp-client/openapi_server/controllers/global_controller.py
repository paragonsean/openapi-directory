from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def delete_global_attribute(request: web.Request, attributekey) -> web.Response:
    """Delete specific global attribute

    Delete global attribute with the specified key. Required: global &#39;servers&#39;.

    :param attributekey: Key of the attribute
    :type attributekey: str

    """
    return web.Response(status=200)


async def delete_global_attributes(request: web.Request, ) -> web.Response:
    """Delete all global attributes

    Delete all global attributes. Required permission: global &#39;servers&#39;.


    """
    return web.Response(status=200)


async def delete_server_privileged_attribute(request: web.Request, serverid, attributekey) -> web.Response:
    """Delete specific privileged attribute of a specific server

    Delete privileged attribute with the specified key of a specific server. Required permission: global &#39;servers&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param attributekey: Key of the attribute
    :type attributekey: str

    """
    return web.Response(status=200)


async def delete_server_privileged_attributes(request: web.Request, serverid) -> web.Response:
    """Delete all privileged attributes of a specific server

    Delete all privileged attributes of a specific server. Required permission: global &#39;servers&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str

    """
    return web.Response(status=200)


async def get_global_attributes(request: web.Request, ) -> web.Response:
    """Get all global attributes

    Returns an array containing all global attributes. Required permission: global &#39;servers&#39;.


    """
    return web.Response(status=200)


async def get_server_privileged_attributes(request: web.Request, serverid) -> web.Response:
    """Get all privileged attributes of a specific server

    Returns an array containing all privileged attributes corresponding to this server. Required permission: global &#39;servers&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str

    """
    return web.Response(status=200)


async def set_global_attributes(request: web.Request, attributes) -> web.Response:
    """Set all global attributes

    Set the global attributes. Prior attributes with keys that are not provided in the body of the request will be deleted. Required permission: global &#39;servers&#39;.

    :param attributes: Array of attributes
    :type attributes: 

    """
    return web.Response(status=200)


async def set_server_privileged_attributes(request: web.Request, serverid, attributes) -> web.Response:
    """Set all privileged attributes of a specific server

    Set the privileged attributes of a specific server. Prior attributes with keys that are not provided in the body of the request will be deleted. Required permission: global &#39;servers&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param attributes: Array of attributes
    :type attributes: 

    """
    return web.Response(status=200)


async def update_global_attributes(request: web.Request, attributes) -> web.Response:
    """Update specified global attributes

    Update the specified global attributes. Prior attributes with keys that are not provided in the body of the request will not be deleted. Required permission: &#39;servers&#39;.

    :param attributes: Array of attributes
    :type attributes: 

    """
    return web.Response(status=200)


async def update_server_privileged_attributes(request: web.Request, serverid, attributes) -> web.Response:
    """Update privileged specified attributes of a specific server

    Update the specified privileged attributes of a specific server. Prior privileged attributes with keys that are not provided in the body of the request will not be deleted. Required permission: global &#39;servers&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param attributes: Array of attributes
    :type attributes: 

    """
    return web.Response(status=200)
