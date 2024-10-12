from typing import List, Dict
from aiohttp import web

from openapi_server.models.chart_row_name_format_types import ChartRowNameFormatTypes
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def chart_rownameformattypes_get(request: web.Request, ) -> web.Response:
    """RowNameFormatTypes: List All Possible Types

    List Types: Use this method to retreive a list of possible options for the RowNameFormatTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Chart object space.


    """
    return web.Response(status=200)


async def chart_rownameformattypes_get_id(request: web.Request, id) -> web.Response:
    """RowNameFormatTypes: Get by Id

    Get by Id: Use this method to retrieve a RowNameFormatTypes object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def chart_rownameformattypes_typeid_get_type_id(request: web.Request, type_id) -> web.Response:
    """RowNameFormatTypes: Get By Type Id

    This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

    :param type_id: 
    :type type_id: int

    """
    return web.Response(status=200)
