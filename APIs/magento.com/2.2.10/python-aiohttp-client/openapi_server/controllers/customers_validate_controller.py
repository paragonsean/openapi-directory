from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_account_management_v1_validate_put_request import CustomerAccountManagementV1ValidatePutRequest
from openapi_server.models.customer_data_validation_results_interface import CustomerDataValidationResultsInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_account_management_v1_validate_put(request: web.Request, body=None) -> web.Response:
    """customers/validate

    Validate customer data.

    :param body: 
    :type body: dict | bytes

    """
    body = CustomerAccountManagementV1ValidatePutRequest.from_dict(body)
    return web.Response(status=200)
