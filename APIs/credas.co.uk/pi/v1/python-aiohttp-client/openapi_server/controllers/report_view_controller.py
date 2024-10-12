from typing import List, Dict
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_report_view_get_report_view_by_reference_id_request import CredasApiModelsReportViewGetReportViewByReferenceIdRequest
from openapi_server.models.credas_api_models_report_view_get_report_view_by_registration_id_request import CredasApiModelsReportViewGetReportViewByRegistrationIdRequest
from openapi_server.models.credas_api_models_report_view_get_report_view_response import CredasApiModelsReportViewGetReportViewResponse
from openapi_server import util


async def get_report_view_by_reference_id(request: web.Request, apikey, body=None) -> web.Response:
    """Retrieves secure links to registration details pages searching by the Reference Id.

    It may return none, one or many (up to 20) matching results.  Each result contains a secure url; UTC date/time of when the link expires; name details of a person associated with the registration.

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Request object
    :type body: dict | bytes

    """
    body = CredasApiModelsReportViewGetReportViewByReferenceIdRequest.from_dict(body)
    return web.Response(status=200)


async def get_report_view_by_registration_id(request: web.Request, apikey, body=None) -> web.Response:
    """Retrieves secure link to registration details page searching by the Registration Id.

    It may return none or one matching result.  Each result contains a secure url; UTC date/time of when the link expires; name details of a person associated with the registration.

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Request object
    :type body: dict | bytes

    """
    body = CredasApiModelsReportViewGetReportViewByRegistrationIdRequest.from_dict(body)
    return web.Response(status=200)
