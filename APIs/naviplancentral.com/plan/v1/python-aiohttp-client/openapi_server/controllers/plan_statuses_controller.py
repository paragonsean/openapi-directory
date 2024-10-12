from typing import List, Dict
from aiohttp import web

from openapi_server.models.plan_statuses_model import PlanStatusesModel
from openapi_server import util


async def plan_statuses_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve plan data statuses

    This operation retrieves the data statuses of the published plan if on demand updates              are enabled

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3)
    :type plan_id: str

    """
    return web.Response(status=200)
