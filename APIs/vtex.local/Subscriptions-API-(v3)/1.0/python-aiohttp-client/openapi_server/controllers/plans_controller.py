from typing import List, Dict
from aiohttp import web

from openapi_server.models.store_plan import StorePlan
from openapi_server import util


async def api_rns_pvt_plans_get(request: web.Request, content_type, accept, periodicity=None, interval=None, page=None, size=None) -> web.Response:
    """List plans

    List plans filtering by some arguments.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param periodicity: Filter plans by available periodicity
    :type periodicity: str
    :param interval: Filter plans by available interval
    :type interval: str
    :param page: Page used for pagination
    :type page: int
    :param size: Page size used for pagination
    :type size: int

    """
    return web.Response(status=200)


async def api_rns_pvt_plans_id_get(request: web.Request, id, content_type, accept) -> web.Response:
    """Get plan details

    This endpoint retrieves a specific plan by its ID.

    :param id: Id from the desired plan
    :type id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)
