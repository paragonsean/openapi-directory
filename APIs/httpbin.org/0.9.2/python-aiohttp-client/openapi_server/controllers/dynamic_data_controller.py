from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def base64_value_get(request: web.Request, value) -> web.Response:
    """Decodes base64url-encoded string.

    

    :param value: 
    :type value: str

    """
    return web.Response(status=200)


async def bytes_nget(request: web.Request, n) -> web.Response:
    """Returns n random bytes generated with given seed

    

    :param n: 
    :type n: int

    """
    return web.Response(status=200)


async def delay_delay_delete(request: web.Request, delay) -> web.Response:
    """Returns a delayed response (max of 10 seconds).

    

    :param delay: 
    :type delay: int

    """
    return web.Response(status=200)


async def delay_delay_get(request: web.Request, delay) -> web.Response:
    """Returns a delayed response (max of 10 seconds).

    

    :param delay: 
    :type delay: int

    """
    return web.Response(status=200)


async def delay_delay_patch(request: web.Request, delay) -> web.Response:
    """Returns a delayed response (max of 10 seconds).

    

    :param delay: 
    :type delay: int

    """
    return web.Response(status=200)


async def delay_delay_post(request: web.Request, delay) -> web.Response:
    """Returns a delayed response (max of 10 seconds).

    

    :param delay: 
    :type delay: int

    """
    return web.Response(status=200)


async def delay_delay_put(request: web.Request, delay) -> web.Response:
    """Returns a delayed response (max of 10 seconds).

    

    :param delay: 
    :type delay: int

    """
    return web.Response(status=200)


async def delay_delay_trace(request: web.Request, delay) -> web.Response:
    """Returns a delayed response (max of 10 seconds).

    

    :param delay: 
    :type delay: int

    """
    return web.Response(status=200)


async def drip_get(request: web.Request, duration=None, numbytes=None, code=None, delay=None) -> web.Response:
    """Drips data over a duration after an optional initial delay.

    

    :param duration: The amount of time (in seconds) over which to drip each byte
    :type duration: 
    :param numbytes: The number of bytes to respond with
    :type numbytes: int
    :param code: The response code that will be returned
    :type code: int
    :param delay: The amount of time (in seconds) to delay before responding
    :type delay: 

    """
    return web.Response(status=200)


async def links_n_offset_get(request: web.Request, n, offset) -> web.Response:
    """Generate a page containing n links to other pages which do the same.

    

    :param n: 
    :type n: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def range_numbytes_get(request: web.Request, numbytes) -> web.Response:
    """Streams n random bytes generated with given seed, at given chunk size per packet.

    

    :param numbytes: 
    :type numbytes: int

    """
    return web.Response(status=200)


async def stream_bytes_nget(request: web.Request, n) -> web.Response:
    """Streams n random bytes generated with given seed, at given chunk size per packet.

    

    :param n: 
    :type n: int

    """
    return web.Response(status=200)


async def stream_nget(request: web.Request, n) -> web.Response:
    """Stream n JSON responses

    

    :param n: 
    :type n: int

    """
    return web.Response(status=200)


async def uuid_get(request: web.Request, ) -> web.Response:
    """Return a UUID4.

    


    """
    return web.Response(status=200)
