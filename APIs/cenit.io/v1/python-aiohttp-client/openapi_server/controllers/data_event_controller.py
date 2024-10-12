from typing import List, Dict
from aiohttp import web

from openapi_server.models.observer import Observer
from openapi_server import util


async def setup_observer_get(request: web.Request, ) -> web.Response:
    """Returns a list of events

    Returns a list of events you&#39;ve previously created. The events are returned in sorted order, with the most recent event appearing first.


    """
    return web.Response(status=200)


async def setup_observer_id_delete(request: web.Request, id) -> web.Response:
    """Delete an event

    Deletes the specified event observer.

    :param id: Observer ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_observer_id_get(request: web.Request, id) -> web.Response:
    """Retrieve an existing event

    Retrieves the details of an existing event. You need only supply the unique event identifier that was returned upon event creation.

    :param id: Observer ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_observer_post(request: web.Request, ) -> web.Response:
    """Create or update an event

    Creates or updates the specified event observer. Any parameters not provided will be left unchanged.


    """
    return web.Response(status=200)
