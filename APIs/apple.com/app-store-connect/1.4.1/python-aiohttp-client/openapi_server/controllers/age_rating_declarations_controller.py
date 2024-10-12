from typing import List, Dict
from aiohttp import web

from openapi_server.models.age_rating_declaration_response import AgeRatingDeclarationResponse
from openapi_server.models.age_rating_declaration_update_request import AgeRatingDeclarationUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def age_rating_declarations_update_instance(request: web.Request, id, body) -> web.Response:
    """age_rating_declarations_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: AgeRatingDeclaration representation
    :type body: dict | bytes

    """
    body = AgeRatingDeclarationUpdateRequest.from_dict(body)
    return web.Response(status=200)
