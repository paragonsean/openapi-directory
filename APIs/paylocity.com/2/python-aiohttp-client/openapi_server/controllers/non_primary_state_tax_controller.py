from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.non_primary_state_tax import NonPrimaryStateTax
from openapi_server import util


async def add_or_update_non_primary_state_tax(request: web.Request, company_id, employee_id, body) -> web.Response:
    """Add/update non-primary state tax

    Sends new or updated employee non-primary state tax information directly to Web Pay.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param body: Non-Primary State Tax Model
    :type body: dict | bytes

    """
    body = NonPrimaryStateTax.from_dict(body)
    return web.Response(status=200)
