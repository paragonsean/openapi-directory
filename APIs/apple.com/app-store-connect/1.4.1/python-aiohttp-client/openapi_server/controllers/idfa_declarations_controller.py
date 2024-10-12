from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.idfa_declaration_create_request import IdfaDeclarationCreateRequest
from openapi_server.models.idfa_declaration_response import IdfaDeclarationResponse
from openapi_server.models.idfa_declaration_update_request import IdfaDeclarationUpdateRequest
from openapi_server import util


async def idfa_declarations_create_instance(request: web.Request, body) -> web.Response:
    """idfa_declarations_create_instance

    

    :param body: IdfaDeclaration representation
    :type body: dict | bytes

    """
    body = IdfaDeclarationCreateRequest.from_dict(body)
    return web.Response(status=200)


async def idfa_declarations_delete_instance(request: web.Request, id) -> web.Response:
    """idfa_declarations_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def idfa_declarations_update_instance(request: web.Request, id, body) -> web.Response:
    """idfa_declarations_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: IdfaDeclaration representation
    :type body: dict | bytes

    """
    body = IdfaDeclarationUpdateRequest.from_dict(body)
    return web.Response(status=200)
