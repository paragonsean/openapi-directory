from typing import List, Dict
from aiohttp import web

from openapi_server.models.goal_model import GoalModel
from openapi_server.models.goals_model import GoalsModel
from openapi_server import util


async def goals_get_by_id_planid(request: web.Request, id, plan_id) -> web.Response:
    """Retrieve goals

    This operation retrieves a goal from the plan.

    :param id: ID of goal to retrieve
    :type id: int
    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def goals_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve goals

    This operation retrieves a list of all of the goals in the plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
