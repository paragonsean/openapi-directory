from typing import List, Dict
from aiohttp import web

from openapi_server.models.service import Service
from openapi_server import util


async def all_lines(request: web.Request, ) -> web.Response:
    """Get all environments

    Get all environments provided by the current Otoroshi instance


    """
    return web.Response(status=200)


async def services_for_a_line(request: web.Request, line) -> web.Response:
    """Get all services for an environment

    Get all services for an environment provided by the current Otoroshi instance

    :param line: The environment where to find services
    :type line: str

    """
    return web.Response(status=200)
