from typing import List, Dict
from aiohttp import web

from openapi_server.models.net_worth_projection_model import NetWorthProjectionModel
from openapi_server.models.net_worth_projections_model import NetWorthProjectionsModel
from openapi_server import util


async def projected_net_worth_get_by_id_planid(request: web.Request, id, plan_id) -> web.Response:
    """Retrieve projected net worth by id

    This operation retrieves an object containing net worth information                 for a single specified year of the projected plan. These are EOY numbers.

    :param id: Index into the list of annual projections
    :type id: int
    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def projected_net_worth_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve projected net worth

    This operation retrieves an object containing net worth information                 for each year of the projected plan. These are EOY numbers.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
