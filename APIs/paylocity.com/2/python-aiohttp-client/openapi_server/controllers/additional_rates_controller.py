from typing import List, Dict
from aiohttp import web

from openapi_server.models.additional_rate import AdditionalRate
from openapi_server.models.error import Error
from openapi_server import util


async def add_or_update_additional_rates(request: web.Request, company_id, employee_id, body) -> web.Response:
    """Add/update additional rates

    Sends new or updated employee additional rates information directly to Web Pay.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param body: Additional Rate Model
    :type body: dict | bytes

    """
    body = AdditionalRate.from_dict(body)
    return web.Response(status=200)
