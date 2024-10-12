from typing import List, Dict
from aiohttp import web

from openapi_server.models.credas_api_models_bank_accounts_account_verification_request import CredasApiModelsBankAccountsAccountVerificationRequest
from openapi_server.models.credas_api_models_bank_accounts_account_verification_response import CredasApiModelsBankAccountsAccountVerificationResponse
from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server import util


async def verify(request: web.Request, apikey, body=None) -> web.Response:
    """Verifies bank account details.

    

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Object containing data required to perform bank account verification.
    :type body: dict | bytes

    """
    body = CredasApiModelsBankAccountsAccountVerificationRequest.from_dict(body)
    return web.Response(status=200)
