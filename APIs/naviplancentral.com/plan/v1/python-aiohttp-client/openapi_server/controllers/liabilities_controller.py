from typing import List, Dict
from aiohttp import web

from openapi_server.models.liabilities_model import LiabilitiesModel
from openapi_server.models.liability_model import LiabilityModel
from openapi_server import util


async def liabilities_get_by_id_planid(request: web.Request, id, plan_id) -> web.Response:
    """Retrieve a liability

    This operation retrieves a liability from the plan.

    :param id: ID of liability to retrieve
    :type id: int
    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def liabilities_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve liabilities

    This operation retrieves a list of all of the liabilities in the plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
