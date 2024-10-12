from typing import List, Dict
from aiohttp import web

from openapi_server.models.bank_account_identification_validation_request import BankAccountIdentificationValidationRequest
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server import util


async def post_validate_bank_account_identification(request: web.Request, body=None) -> web.Response:
    """Validate a bank account

    Validates bank account identification details. You can use this endpoint to validate bank account details before you [make a transfer](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers) or [create a transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments).

    :param body: 
    :type body: dict | bytes

    """
    body = BankAccountIdentificationValidationRequest.from_dict(body)
    return web.Response(status=200)
