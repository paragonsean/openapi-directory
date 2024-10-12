from typing import List, Dict
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_web_verifications_get_web_verifications_by_reference_id_request import CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest
from openapi_server.models.credas_api_models_web_verifications_get_web_verifications_by_registration_id_request import CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest
from openapi_server.models.credas_api_models_web_verifications_get_web_verifications_response import CredasApiModelsWebVerificationsGetWebVerificationsResponse
from openapi_server import util


async def get_web_verifications_by_reference_id(request: web.Request, apikey, body=None) -> web.Response:
    """Retrieves secure links to web verification pages searching by the Reference Id.

    It may return none, one or many (up to 20) matching results.  Each result contains a secure url; UTC date/time of when the link expires; name details of a person associated with the registration.

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: 
    :type body: dict | bytes

    """
    body = CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest.from_dict(body)
    return web.Response(status=200)


async def get_web_verifications_by_registration_id(request: web.Request, apikey, body=None) -> web.Response:
    """Retrieves secure link to web verification page searching by the Registration Id.

    It may return none or one matching result.  Each result contains a secure url; UTC date/time of when the link expires; name details of a person associated with the registration.

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: 
    :type body: dict | bytes

    """
    body = CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest.from_dict(body)
    return web.Response(status=200)
