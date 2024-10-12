from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.intervention import Intervention
from openapi_server import util


async def get_intervention(request: web.Request, id) -> web.Response:
    """get_intervention

    Returns intervention details

    :param id: ID of the intervention
    :type id: str

    """
    return web.Response(status=200)
