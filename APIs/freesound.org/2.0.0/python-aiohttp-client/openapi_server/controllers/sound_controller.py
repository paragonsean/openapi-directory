from typing import List, Dict
from aiohttp import web

from openapi_server.models.sound import Sound
from openapi_server import util


async def get_sound_by_id(request: web.Request, sound_id) -> web.Response:
    """Details of a sound

    This resource allows the retrieval of detailed information about a sound.

    :param sound_id: ID of the sound that needs to be fetched
    :type sound_id: int

    """
    return web.Response(status=200)
