from typing import List, Dict
from aiohttp import web

from openapi_server.models.chart_data_points import ChartDataPoints
from openapi_server import util


async def chart_datapoints_get_id(request: web.Request, id) -> web.Response:
    """DataPoints: Get by Id

    Get by Id: Use this method to retrieve a DataPoints object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
