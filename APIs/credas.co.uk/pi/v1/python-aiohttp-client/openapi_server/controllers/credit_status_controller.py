from typing import List, Dict
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_status_checks_status_check import CredasApiModelsStatusChecksStatusCheck
from openapi_server.models.credas_api_models_status_checks_status_check_request import CredasApiModelsStatusChecksStatusCheckRequest
from openapi_server import util


async def check_credit_status(request: web.Request, apikey, body=None) -> web.Response:
    """Check includes identifying bankruptcy, insolvency, CCJ&#39;s or Company Directorship.

    

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Object containing data required to perform the check.
    :type body: dict | bytes

    """
    body = CredasApiModelsStatusChecksStatusCheckRequest.from_dict(body)
    return web.Response(status=200)
