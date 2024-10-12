from typing import List, Dict
from aiohttp import web

from openapi_server.models.assets_funding_goal_model import AssetsFundingGoalModel
from openapi_server.models.needs_vs_abilities_model import NeedsVsAbilitiesModel
from openapi_server import util


async def projected_goals_get_assets_funding_goals_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve assets funding goals over time

    This operation retrieves the assets funding each goal throughout the plan years

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def projected_goals_get_needs_vs_abilities_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve needs vs abilities data

    This operation retrieves a needs and abilities data for all goals throughout                the plan years.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
