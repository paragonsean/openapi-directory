from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_credit_data_credit_limit_interface import CompanyCreditDataCreditLimitInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_credit_credit_limit_repository_v1_get_get(request: web.Request, credit_id, reload=None) -> web.Response:
    """companyCredits/{creditId}

    Returns data on the credit limit for a specified credit limit ID.

    :param credit_id: 
    :type credit_id: int
    :param reload: [optional]
    :type reload: bool

    """
    return web.Response(status=200)
