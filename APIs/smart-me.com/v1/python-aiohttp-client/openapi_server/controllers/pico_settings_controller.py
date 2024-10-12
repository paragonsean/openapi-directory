from typing import List, Dict
from aiohttp import web

from openapi_server.models.pico_settings_dto import PicoSettingsDto
from openapi_server import util


async def pico_settings_get(request: web.Request, id) -> web.Response:
    """GET: api/pico/settings                            Returns the settings of a pico charging station.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
