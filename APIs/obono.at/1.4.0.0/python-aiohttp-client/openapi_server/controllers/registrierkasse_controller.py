from typing import List, Dict
from aiohttp import web

from openapi_server.models.registrierkasse import Registrierkasse
from openapi_server import util


async def get_dep(request: web.Request, registrierkasse_uuid) -> web.Response:
    """get_dep

    Generates a DEP file.

    :param registrierkasse_uuid: The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to retrieve the DEP file.
    :type registrierkasse_uuid: str

    """
    return web.Response(status=200)


async def get_registrierkasse(request: web.Request, registrierkasse_uuid) -> web.Response:
    """get_registrierkasse

    Returns information about a particular &#x60;Registrierkasse&#x60;.

    :param registrierkasse_uuid: The &#x60;_uuid&#x60; of a particular &#x60;Registrierkasse&#x60; to fetch.
    :type registrierkasse_uuid: str

    """
    return web.Response(status=200)
