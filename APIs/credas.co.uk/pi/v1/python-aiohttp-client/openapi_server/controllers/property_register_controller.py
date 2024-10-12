from typing import List, Dict
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_property_register_property_register_check_request import CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest
from openapi_server.models.credas_api_models_property_register_property_register_check_response import CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse
from openapi_server import util


async def add_property_register_check(request: web.Request, apikey, body=None) -> web.Response:
    """Creates new property registry check against the registration.

    

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Object containing check details.
    :type body: dict | bytes

    """
    body = CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest.from_dict(body)
    return web.Response(status=200)


async def get_property_register_check_result(request: web.Request, id, apikey) -> web.Response:
    """Retrieves property registry check associated with the registration.

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)
