from typing import List, Dict
from aiohttp import web

from openapi_server.models.defined_benefit_pension_model import DefinedBenefitPensionModel
from openapi_server.models.defined_benefit_pensions_model import DefinedBenefitPensionsModel
from openapi_server import util


async def defined_benefit_pensions_get_by_id_planid(request: web.Request, id, plan_id) -> web.Response:
    """Retrieve a definedBenefitPension

    This operation retrieves a defined benefit pension from the plan.

    :param id: ID of defined benefit pension to retrieve
    :type id: int
    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def defined_benefit_pensions_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve defined benefit pensions

    This operation retrieves a list of all of the defined benefit pensions in the plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)
