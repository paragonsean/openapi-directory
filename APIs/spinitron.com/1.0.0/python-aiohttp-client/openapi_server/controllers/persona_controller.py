from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.persona import Persona
from openapi_server.models.personas_get200_response import PersonasGet200Response
from openapi_server import util


async def personas_get(request: web.Request, name=None, count=None, page=None, fields=None, expand=None) -> web.Response:
    """Get Personas

    

    :param name: Filter by Persona name
    :type name: str
    :param count: Amount of items to return
    :type count: int
    :param page: Offset, used together with count
    :type page: int
    :param fields: Allows to select only needed fields
    :type fields: List[str]
    :param expand: Allows to select extra fields
    :type expand: List[str]

    """
    return web.Response(status=200)


async def personas_id_get(request: web.Request, id, fields=None, expand=None) -> web.Response:
    """Get Persona by id

    

    :param id: 
    :type id: int
    :param fields: Allows to select only needed fields
    :type fields: List[str]
    :param expand: Allows to select extra fields
    :type expand: List[str]

    """
    return web.Response(status=200)
