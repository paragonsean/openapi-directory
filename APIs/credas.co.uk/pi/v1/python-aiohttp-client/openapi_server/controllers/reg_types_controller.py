from typing import List, Dict
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_reg_types_reg_type import CredasApiModelsRegTypesRegType
from openapi_server import util


async def get_all(request: web.Request, apikey) -> web.Response:
    """Gets all available RegTypes.

    

    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)
