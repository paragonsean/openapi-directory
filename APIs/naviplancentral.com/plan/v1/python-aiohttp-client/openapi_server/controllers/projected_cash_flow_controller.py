from typing import List, Dict
from aiohttp import web

from openapi_server.models.cash_flow_projection_model import CashFlowProjectionModel
from openapi_server.models.cash_flow_projections_model import CashFlowProjectionsModel
from openapi_server import util


async def projected_cash_flow_get_by_id_planid(request: web.Request, id, plan_id) -> web.Response:
    """Retrieve projected cash flow by id

    This operation retrieves an object containing cash flow information                 for a single specified year of the projected plan.

    :param id: Index into the list of annual projections
    :type id: int
    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def projected_cash_flow_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve projected cash flow

    This operation retrieves an object containing cash flow information                 for each year of the projected plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
