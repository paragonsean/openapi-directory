from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact_formats import ArtifactFormats
from openapi_server.models.change_log_item import ChangeLogItem
from openapi_server.models.event_type import EventType
from openapi_server import util


async def artifact_formats_get(request: web.Request, ) -> web.Response:
    """Artifact formats

    List the available artifact formats


    """
    return web.Response(status=200)


async def change_log_get(request: web.Request, ) -> web.Response:
    """Recent changes

    The Contribly change log.


    """
    return web.Response(status=200)


async def event_types_get(request: web.Request, ) -> web.Response:
    """Event types

    List available notification event types


    """
    return web.Response(status=200)
