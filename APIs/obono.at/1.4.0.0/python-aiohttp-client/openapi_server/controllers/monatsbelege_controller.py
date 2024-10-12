from typing import List, Dict
from aiohttp import web

from openapi_server.models.monatsbeleg import Monatsbeleg
from openapi_server import util


async def get_monatsbelege(request: web.Request, registrierkasse_uuid, year=None, month=None) -> web.Response:
    """get_monatsbelege

    Returns a list of &#x60;Monatsbelege&#x60;.

    :param registrierkasse_uuid: The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60;.
    :type registrierkasse_uuid: str
    :param year: 
    :type year: int
    :param month: 
    :type month: int

    """
    return web.Response(status=200)
