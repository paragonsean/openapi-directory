from typing import List, Dict
from aiohttp import web

from openapi_server.models.destination import Destination
from openapi_server.models.source import Source
from openapi_server import util


async def destinations_get(request: web.Request, ) -> web.Response:
    """destinations_get

    Returns a list of currently available destinations. Possible destinations are box - sending data to a remote box, and scu - sending data a receiving SCP.


    """
    return web.Response(status=200)


async def sources_get(request: web.Request, ) -> web.Response:
    """sources_get

    Returns a list of currently available data sources. Possible source types are user - data imported by an API call by a user, box - data received from a remote box, directory - data imported via a watched directory, import - data imported into slicebox using import sessions, or scp - data received from a PACS.


    """
    return web.Response(status=200)


async def system_health_get(request: web.Request, ) -> web.Response:
    """system_health_get

    No-op route for checking whether the service is alive or not


    """
    return web.Response(status=200)


async def system_stop_post(request: web.Request, ) -> web.Response:
    """system_stop_post

    stop and shut down slicebox


    """
    return web.Response(status=200)
