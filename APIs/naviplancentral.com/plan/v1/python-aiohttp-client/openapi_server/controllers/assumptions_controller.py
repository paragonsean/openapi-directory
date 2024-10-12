from typing import List, Dict
from aiohttp import web

from openapi_server.models.assumptions_model import AssumptionsModel
from openapi_server import util


async def assumptions_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve plan assumptions

    This operation retrieves an object containing all assumptions for the specified plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
