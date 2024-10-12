from typing import List, Dict
from aiohttp import web

from openapi_server.models.projected_annual_summaries_model import ProjectedAnnualSummariesModel
from openapi_server.models.projected_annual_summary_model import ProjectedAnnualSummaryModel
from openapi_server import util


async def projected_annual_summary_get_by_id_planid(request: web.Request, id, plan_id) -> web.Response:
    """Retrieve projected annual summary by id

    This operation retrieves an object containing annual summary information                 for a single specified year of the projected plan.

    :param id: Index into the list of annual projections
    :type id: int
    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def projected_annual_summary_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve projected annual summaries

    This operation retrieves an object containing annual summary information                 for each year of the projected plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
