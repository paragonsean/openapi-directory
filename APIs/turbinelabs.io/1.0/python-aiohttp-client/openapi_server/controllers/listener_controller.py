from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.listener import Listener
from openapi_server.models.listener_create import ListenerCreate
from openapi_server.models.listener_result import ListenerResult
from openapi_server.models.multi_listener_result import MultiListenerResult
from openapi_server import util


async def listener_get(request: web.Request, filters=None) -> web.Response:
    """list listeners

    Get a list of listeners

    :param filters: A JSON encoded array of ListenerFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ListenerFilter will be included. 
    :type filters: str

    """
    return web.Response(status=200)


async def listener_listener_key_delete(request: web.Request, listener_key, checksum) -> web.Response:
    """delete listener

    Delete existing listener

    :param listener_key: the listener key
    :type listener_key: str
    :param checksum: the current checksum of the listener to be deleted
    :type checksum: str

    """
    return web.Response(status=200)


async def listener_listener_key_get(request: web.Request, listener_key) -> web.Response:
    """get listener

    Get details for a single listener

    :param listener_key: the listener key
    :type listener_key: str

    """
    return web.Response(status=200)


async def listener_listener_key_put(request: web.Request, listener_key, listener) -> web.Response:
    """modify listener

    Modify an existing listener

    :param listener_key: the listener key
    :type listener_key: str
    :param listener: the listener to modify
    :type listener: dict | bytes

    """
    listener = Listener.from_dict(listener)
    return web.Response(status=200)


async def listener_post(request: web.Request, listener) -> web.Response:
    """create listener

    Create a new listener

    :param listener: the listener to create
    :type listener: dict | bytes

    """
    listener = ListenerCreate.from_dict(listener)
    return web.Response(status=200)
