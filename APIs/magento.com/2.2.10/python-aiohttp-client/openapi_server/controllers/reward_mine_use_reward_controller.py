from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def reward_reward_management_v1_set_post(request: web.Request, ) -> web.Response:
    """reward/mine/use-reward

    Set reward points to quote


    """
    return web.Response(status=200)
