from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_credit_credit_limit_repository_v1_save_put_request import CompanyCreditCreditLimitRepositoryV1SavePutRequest
from openapi_server.models.company_credit_data_credit_limit_interface import CompanyCreditDataCreditLimitInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_credit_credit_limit_repository_v1_save_put(request: web.Request, id, body=None) -> web.Response:
    """companyCredits/{id}

    Update the following company credit attributes: credit currency, credit limit and setting to exceed credit.

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompanyCreditCreditLimitRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)
