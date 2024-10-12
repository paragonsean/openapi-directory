from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def calculations_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve Monte Carlo results from standalone calc service

    Currently just stubbed out, POC in development

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
