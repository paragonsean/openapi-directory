from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_child(request: web.Request, uuid) -> web.Response:
    """get_child

    Get child UUID(s) from a specified project or publisher UUID.

    :param uuid: 
    :type uuid: str

    """
    return web.Response(status=200)


async def get_generate_uuid(request: web.Request, ) -> web.Response:
    """get_generate_uuid

    Generate an UUID version 4 RFC4122-compliant.


    """
    return web.Response(status=200)


async def get_info(request: web.Request, ) -> web.Response:
    """get_info

    Get information about the CyCAT backend services including status, overall statistics and version.


    """
    return web.Response(status=200)


async def get_list_project(request: web.Request, start, end) -> web.Response:
    """get_list_project

    List projects registered in CyCAT by pagination (start,end).

    :param start: 
    :type start: int
    :param end: 
    :type end: int

    """
    return web.Response(status=200)


async def get_list_publisher(request: web.Request, start, end) -> web.Response:
    """get_list_publisher

    List publishers registered in CyCAT by pagination (start,end).

    :param start: 
    :type start: int
    :param end: 
    :type end: int

    """
    return web.Response(status=200)


async def get_lookup(request: web.Request, uuid) -> web.Response:
    """get_lookup

    Lookup UUID registered in CyCAT.

    :param uuid: 
    :type uuid: str

    """
    return web.Response(status=200)


async def get_namespacefinduuid(request: web.Request, namespace, namespaceid) -> web.Response:
    """get_namespacefinduuid

    Get all known UUID for a given namespace id.

    :param namespace: 
    :type namespace: str
    :param namespaceid: 
    :type namespaceid: str

    """
    return web.Response(status=200)


async def get_namespacegetall(request: web.Request, ) -> web.Response:
    """get_namespacegetall

    List all known namespaces.


    """
    return web.Response(status=200)


async def get_namespacegetid(request: web.Request, namespace) -> web.Response:
    """get_namespacegetid

    Get all ID from a given namespace.

    :param namespace: 
    :type namespace: str

    """
    return web.Response(status=200)


async def get_parent(request: web.Request, uuid) -> web.Response:
    """get_parent

    Get parent UUID(s) from a specified project or item UUID.

    :param uuid: 
    :type uuid: str

    """
    return web.Response(status=200)


async def get_relationships(request: web.Request, uuid) -> web.Response:
    """get_relationships

    Get relationship(s) UUID from a specified UUID.

    :param uuid: 
    :type uuid: str

    """
    return web.Response(status=200)


async def get_relationshipsexpanded(request: web.Request, uuid) -> web.Response:
    """get_relationshipsexpanded

    Get relationship(s) UUID from a specified UUID including the relationships meta information.

    :param uuid: 
    :type uuid: str

    """
    return web.Response(status=200)


async def get_search(request: web.Request, searchquery) -> web.Response:
    """get_search

    Full-text search in CyCAT and return matching UUID.

    :param searchquery: 
    :type searchquery: str

    """
    return web.Response(status=200)


async def post_propose(request: web.Request, ) -> web.Response:
    """post_propose

    Propose new resource to CyCAT.


    """
    return web.Response(status=200)
