from typing import List, Dict
from aiohttp import web

from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_health_question_definition_response import FetchHealthQuestionDefinitionResponse
from openapi_server.models.fetch_health_question_definitions_response import FetchHealthQuestionDefinitionsResponse
from openapi_server import util


async def fetch_health_question_definition(request: web.Request, id) -> web.Response:
    """Get a health question definition

    Get a health question definition by id

    :param id: Health question definition identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_health_question_definitions(request: web.Request, ) -> web.Response:
    """List health question definitions

    Get a list of all health question definitions


    """
    return web.Response(status=200)
