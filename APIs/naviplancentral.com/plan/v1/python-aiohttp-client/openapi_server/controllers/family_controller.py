from typing import List, Dict
from aiohttp import web

from openapi_server.models.family_model import FamilyModel
from openapi_server import util


async def family_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve family

    This operation retrieves an object containing all familymembers for the specified plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
