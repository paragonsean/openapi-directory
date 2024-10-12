from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def dweet_for_thing_post(request: web.Request, thing, content, key=None) -> web.Response:
    """Create a dweet for a thing.

    

    :param thing: A unique name of a thing. It is recommended that you use a GUID as to avoid name collisions.
    :type thing: str
    :param content: The actual content of the string. Can be any valid JSON string.
    :type content: str
    :param key: A valid key for a locked thing. If the thing is not locked, this can be ignored.
    :type key: str

    """
    return web.Response(status=200)


async def dweet_quietly_for_thing_post(request: web.Request, thing, content, key=None) -> web.Response:
    """Create a dweet for a thing.  This method differs from /dweet/for/{thing} only in that successful dweets result in an HTTP 204 response rather than the typical verbose response.

    

    :param thing: A unique name of a thing. It is recommended that you use a GUID as to avoid name collisions.
    :type thing: str
    :param content: The actual content of the string. Can be any valid JSON string.
    :type content: str
    :param key: A valid key for a locked thing. If the thing is not locked, this can be ignored.
    :type key: str

    """
    return web.Response(status=200)


async def get_dweets_for_thing_get(request: web.Request, thing, key=None) -> web.Response:
    """Read the last 5 cached dweets for a thing.

    

    :param thing: A unique name of a thing.
    :type thing: str
    :param key: A valid key for a locked thing. If the thing is not locked, this can be ignored.
    :type key: str

    """
    return web.Response(status=200)


async def get_latest_dweet(request: web.Request, thing, key=None) -> web.Response:
    """Read the latest dweet for a thing.

    

    :param thing: A unique name of a thing.
    :type thing: str
    :param key: A valid key for a locked thing. If the thing is not locked, this can be ignored.
    :type key: str

    """
    return web.Response(status=200)


async def listen_for_dweets(request: web.Request, thing) -> web.Response:
    """Listen for dweets from a thing.

    Sorry, this function uses HTTP chunked responses and cannot be tested here. Try something like: &lt;pre&gt;curl --raw https://dweet.io/listen/for/dweets/from/{thing}&lt;/pre&gt;

    :param thing: 
    :type thing: str

    """
    return web.Response(status=200)
