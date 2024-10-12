from typing import List, Dict
from aiohttp import web

from openapi_server.models.chart_row_collections import ChartRowCollections
from openapi_server import util


async def chart_rowcollections_get_id(request: web.Request, id) -> web.Response:
    """RowCollections: Get by Id

    Get by Id: Use this method to retrieve a RowCollections object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
