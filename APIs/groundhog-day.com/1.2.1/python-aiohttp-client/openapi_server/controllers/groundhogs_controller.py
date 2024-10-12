from typing import List, Dict
from aiohttp import web

from openapi_server.models.groundhog200_response import Groundhog200Response
from openapi_server.models.groundhog400_response import Groundhog400Response
from openapi_server.models.groundhogs200_response import Groundhogs200Response
from openapi_server import util


async def groundhog(request: web.Request, slug) -> web.Response:
    """Get a groundhog by slug

    Returns a prognosticating animal and its known predictions.

    :param slug: Groundhog name in kebab-case: (eg, lucy-the-lobster)
    :type slug: str

    """
    return web.Response(status=200)


async def groundhogs(request: web.Request, country=None, is_groundhog=None) -> web.Response:
    """Get all groundhogs

    Returns all prognosticating animals with their known predictions.

    :param country: Filter groundhogs by country of origin (USA or Canada).
    :type country: str
    :param is_groundhog: Filter groundhogs by type (actual, alive groundhogs, or other prognosticators)
    :type is_groundhog: str

    """
    return web.Response(status=200)
