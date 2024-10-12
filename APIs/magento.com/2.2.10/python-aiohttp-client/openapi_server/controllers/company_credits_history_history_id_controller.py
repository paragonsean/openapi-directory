from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_credit_credit_history_management_v1_update_put_request import CompanyCreditCreditHistoryManagementV1UpdatePutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_credit_credit_history_management_v1_update_put(request: web.Request, history_id, body=None) -> web.Response:
    """companyCredits/history/{historyId}

    Update the PO Number and/or comment for a Reimburse transaction.

    :param history_id: 
    :type history_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CompanyCreditCreditHistoryManagementV1UpdatePutRequest.from_dict(body)
    return web.Response(status=200)
