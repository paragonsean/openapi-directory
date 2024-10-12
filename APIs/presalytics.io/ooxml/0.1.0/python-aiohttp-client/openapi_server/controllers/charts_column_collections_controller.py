from typing import List, Dict
from aiohttp import web

from openapi_server.models.chart_column_collections import ChartColumnCollections
from openapi_server import util


async def chart_columncollections_get_id(request: web.Request, id) -> web.Response:
    """ColumnCollections: Get by Id

    Get by Id: Use this method to retrieve a ColumnCollections object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
