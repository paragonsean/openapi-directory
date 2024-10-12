from typing import List, Dict
from aiohttp import web

from openapi_server.models.plan_information_model import PlanInformationModel
from openapi_server import util


async def plan_information_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve plan information

    This operation retrieves the high level plan information for a given plan

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
