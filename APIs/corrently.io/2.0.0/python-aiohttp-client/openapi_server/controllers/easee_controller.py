from typing import List, Dict
from aiohttp import web

from openapi_server.models.easee_charger import EaseeCharger
from openapi_server import util


async def easee_sessions(request: web.Request, username=None, password=None) -> web.Response:
    """Returns lastSession info for all easee wallboxes (chargers) given user has access to.

    Refer to easee.cloud API for details. 

    :param username: Username as used on easy.cloud
    :type username: str
    :param password: Password as used on easy.cloud
    :type password: str

    """
    return web.Response(status=200)
