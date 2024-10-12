from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def rma_track_management_v1_remove_track_by_id_delete(request: web.Request, id, track_id) -> web.Response:
    """returns/{id}/tracking-numbers/{trackId}

    Remove track by id

    :param id: 
    :type id: int
    :param track_id: 
    :type track_id: int

    """
    return web.Response(status=200)
