from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_credit_data_credit_limit_interface import CompanyCreditDataCreditLimitInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_credit_credit_limit_management_v1_get_credit_by_company_id_get(request: web.Request, company_id) -> web.Response:
    """companyCredits/company/{companyId}

    Returns data on the credit limit for a specified company.

    :param company_id: 
    :type company_id: int

    """
    return web.Response(status=200)
