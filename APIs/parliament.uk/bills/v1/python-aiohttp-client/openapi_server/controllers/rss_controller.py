from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def api_v1_rss_allbills_rss_get(request: web.Request, ) -> web.Response:
    """Returns an Rss feed of all Bills.

    


    """
    return web.Response(status=200)


async def api_v1_rss_bills_id_rss_get(request: web.Request, id) -> web.Response:
    """Returns an Rss feed of a certain Bill.

    

    :param id: Id of Bill
    :type id: int

    """
    return web.Response(status=200)


async def api_v1_rss_privatebills_rss_get(request: web.Request, ) -> web.Response:
    """Returns an Rss feed of private Bills.

    


    """
    return web.Response(status=200)


async def api_v1_rss_publicbills_rss_get(request: web.Request, ) -> web.Response:
    """Returns an Rss feed of public Bills.

    


    """
    return web.Response(status=200)
