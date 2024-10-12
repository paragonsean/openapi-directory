from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_children(request: web.Request, sha1, count, cursor) -> web.Response:
    """get_children

    Return children from a given SHA1.  A number of element to return and an offset must be given. If not set it will be the 100 first elements. A cursor must be given to paginate over. The starting cursor is 0.

    :param sha1: 
    :type sha1: str
    :param count: 
    :type count: int
    :param cursor: 
    :type cursor: str

    """
    return web.Response(status=200)


async def get_info(request: web.Request, ) -> web.Response:
    """get_info

    Info about the hashlookup database


    """
    return web.Response(status=200)


async def get_lookup_md5(request: web.Request, md5) -> web.Response:
    """get_lookup_md5

    Lookup MD5.

    :param md5: 
    :type md5: str

    """
    return web.Response(status=200)


async def get_lookup_sha1(request: web.Request, sha1) -> web.Response:
    """get_lookup_sha1

    Lookup SHA-1.

    :param sha1: 
    :type sha1: str

    """
    return web.Response(status=200)


async def get_lookup_sha256(request: web.Request, sha256) -> web.Response:
    """get_lookup_sha256

    Lookup SHA-256.

    :param sha256: 
    :type sha256: str

    """
    return web.Response(status=200)


async def get_parents(request: web.Request, sha1, count, cursor) -> web.Response:
    """get_parents

    Return parents from a given SHA1. A number of element to return and an offset must be given. If not set it will be the 100 first elements. A cursor must be given to paginate over. The starting cursor is 0.

    :param sha1: 
    :type sha1: str
    :param count: 
    :type count: int
    :param cursor: 
    :type cursor: str

    """
    return web.Response(status=200)


async def get_session_create(request: web.Request, name) -> web.Response:
    """get_session_create

    Create a session key to keep search context. The session is attached to a name. After the session is created, the header &#x60;hashlookup_session&#x60; can be set to the session name.

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def get_session_matches(request: web.Request, name) -> web.Response:
    """get_session_matches

    Return set of matching and non-matching hashes from a session.

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def get_stattop(request: web.Request, ) -> web.Response:
    """get_stattop

    Return the top 100 of most queried values.


    """
    return web.Response(status=200)


async def post_bulkmd5(request: web.Request, ) -> web.Response:
    """post_bulkmd5

    Bulk search of MD5 hashes in a JSON array with the key &#39;hashes&#39;.


    """
    return web.Response(status=200)


async def post_bulksha1(request: web.Request, ) -> web.Response:
    """post_bulksha1

    Bulk search of SHA1 hashes in a JSON array with the &#39;hashes&#39;.


    """
    return web.Response(status=200)
