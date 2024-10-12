from typing import List, Dict
from aiohttp import web

from openapi_server.models.net_worth_model import NetWorthModel
from openapi_server import util


async def net_worth_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve net worth

    This operation retrieves an object containing net worth values for specific dates within the plan:                * Plan Start Date                * Retirement Date                * Plan End Date.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
