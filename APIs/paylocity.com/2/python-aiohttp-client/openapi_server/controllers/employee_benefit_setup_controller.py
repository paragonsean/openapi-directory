from typing import List, Dict
from aiohttp import web

from openapi_server.models.benefit_setup import BenefitSetup
from openapi_server.models.error import Error
from openapi_server import util


async def update_or_add_employee_benefit_setup(request: web.Request, company_id, employee_id, body) -> web.Response:
    """Add/update employee&#39;s benefit setup

    Sends new or updated employee benefit setup information directly to Web Pay.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param body: BenefitSetup Model
    :type body: dict | bytes

    """
    body = BenefitSetup.from_dict(body)
    return web.Response(status=200)
