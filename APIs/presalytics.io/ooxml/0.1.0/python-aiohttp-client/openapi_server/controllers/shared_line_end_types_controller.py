from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.shared_line_end_types import SharedLineEndTypes
from openapi_server import util


async def shared_lineendtypes_get(request: web.Request, ) -> web.Response:
    """LineEndTypes: List All Possible Types

    List Types: Use this method to retreive a list of possible options for the LineEndTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.


    """
    return web.Response(status=200)


async def shared_lineendtypes_get_id(request: web.Request, id) -> web.Response:
    """LineEndTypes: Get by Id

    Get by Id: Use this method to retrieve a LineEndTypes object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def shared_lineendtypes_typeid_get_type_id(request: web.Request, type_id) -> web.Response:
    """LineEndTypes: Get By Type Id

    This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

    :param type_id: 
    :type type_id: int

    """
    return web.Response(status=200)
