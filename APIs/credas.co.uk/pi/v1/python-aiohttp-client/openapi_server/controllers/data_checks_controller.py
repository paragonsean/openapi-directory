from typing import List, Dict
from aiohttp import web

from openapi_server.models.credas_api_models_data_check_add_data_check_request import CredasApiModelsDataCheckAddDataCheckRequest
from openapi_server.models.credas_api_models_data_check_add_data_check_response import CredasApiModelsDataCheckAddDataCheckResponse
from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server import util


async def add_data_check(request: web.Request, apikey, body=None) -> web.Response:
    """Creates new data check against a specified registration.

    

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Object containing data check details.
    :type body: dict | bytes

    """
    body = CredasApiModelsDataCheckAddDataCheckRequest.from_dict(body)
    return web.Response(status=200)
