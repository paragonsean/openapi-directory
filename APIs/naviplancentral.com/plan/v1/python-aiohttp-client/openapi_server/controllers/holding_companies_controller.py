from typing import List, Dict
from aiohttp import web

from openapi_server.models.holding_companies_model import HoldingCompaniesModel
from openapi_server.models.holding_company_model import HoldingCompanyModel
from openapi_server import util


async def holding_companies_get_by_id_planid(request: web.Request, id, plan_id) -> web.Response:
    """Retrieve a holding company

    This operation retrieves a holding company from the plan.

    :param id: ID of holding company to retrieve
    :type id: int
    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def holding_companies_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve holding companies

    This operation retrieves a list of all of the holding companies in the plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
