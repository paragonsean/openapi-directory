from typing import List, Dict
from aiohttp import web

from openapi_server.models.direct_deposit import DirectDeposit
from openapi_server.models.error import Error
from openapi_server import util


async def get_all_direct_deposit(request: web.Request, company_id, employee_id) -> web.Response:
    """Get All Direct Deposit

    Get All Direct Deposit returns main direct deposit and all additional direct depositsfor the selected employee.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str

    """
    return web.Response(status=200)
