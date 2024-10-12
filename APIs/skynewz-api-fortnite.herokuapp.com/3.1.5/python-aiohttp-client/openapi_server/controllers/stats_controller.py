from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_get_default_response import CheckGetDefaultResponse
from openapi_server.models.stats_id_plateform_id_get200_response import StatsIdPlateformIdGet200Response
from openapi_server import util


async def stats_id_plateform_id_get(request: web.Request, plateform, id) -> web.Response:
    """Get user&#39;s stats by user id

    

    :param plateform: Playing plateform, can be xb1, ps4 or pc
    :type plateform: str
    :param id: Player ID
    :type id: str

    """
    return web.Response(status=200)


async def stats_plateform_username_get(request: web.Request, plateform, username) -> web.Response:
    """Get user&#39;s stats by username

    

    :param plateform: Playing plateform, can be xb1, ps4 or pc
    :type plateform: str
    :param username: Player username
    :type username: str

    """
    return web.Response(status=200)
