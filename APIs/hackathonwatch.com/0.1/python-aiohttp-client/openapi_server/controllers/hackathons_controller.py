from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def g_et_hackathons_coming_format(request: web.Request, page=None) -> web.Response:
    """Return a list of coming hackathons

    

    :param page: Specify the page of coming hackathons.
    :type page: int

    """
    return web.Response(status=200)


async def g_et_hackathons_id_format(request: web.Request, id) -> web.Response:
    """Return the detail of a given hackathon

    

    :param id: ID of the hackathon for detail information
    :type id: int

    """
    return web.Response(status=200)
