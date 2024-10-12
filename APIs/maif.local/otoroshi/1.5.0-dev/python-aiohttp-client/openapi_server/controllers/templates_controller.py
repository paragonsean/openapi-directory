from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.group import Group
from openapi_server.models.service import Service
from openapi_server import util


async def initiate_api_key(request: web.Request, ) -> web.Response:
    """Get a template of an Otoroshi Api Key

    Get a template of an Otoroshi Api Key. The generated entity is not persisted


    """
    return web.Response(status=200)


async def initiate_service(request: web.Request, ) -> web.Response:
    """Get a template of an Otoroshi service descriptor

    Get a template of an Otoroshi service descriptor. The generated entity is not persisted


    """
    return web.Response(status=200)


async def initiate_service_group(request: web.Request, ) -> web.Response:
    """Get a template of an Otoroshi service group

    Get a template of an Otoroshi service group. The generated entity is not persisted


    """
    return web.Response(status=200)
