from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.slide_group_element_types import SlideGroupElementTypes
from openapi_server import util


async def slides_groupelementtypes_get(request: web.Request, ) -> web.Response:
    """GroupElementTypes: List All Possible Types

    List Types: Use this method to retreive a list of possible options for the GroupElementTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Slides object space.


    """
    return web.Response(status=200)


async def slides_groupelementtypes_get_id(request: web.Request, id) -> web.Response:
    """GroupElementTypes: Get by Id

    Get by Id: Use this method to retrieve a GroupElementTypes object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def slides_groupelementtypes_typeid_get_type_id(request: web.Request, type_id) -> web.Response:
    """GroupElementTypes: Get By Type Id

    This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

    :param type_id: 
    :type type_id: int

    """
    return web.Response(status=200)
