from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_credit_credit_balance_management_v1_decrease_post_request import CompanyCreditCreditBalanceManagementV1DecreasePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_credit_credit_balance_management_v1_decrease_post(request: web.Request, credit_id, body=None) -> web.Response:
    """companyCredits/{creditId}/decreaseBalance

    Decreases the company credit with an Update, Reimburse, or Purchase transaction. This transaction increases company&#39;s outstanding balance and decreases company&#39;s available credit.

    :param credit_id: 
    :type credit_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CompanyCreditCreditBalanceManagementV1DecreasePostRequest.from_dict(body)
    return web.Response(status=200)
