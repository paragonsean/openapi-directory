from typing import List, Dict
from aiohttp import web

from openapi_server.models.chart_chart_data import ChartChartData
from openapi_server import util


async def chart_chartdata_get_id(request: web.Request, id) -> web.Response:
    """ChartData: Get by Id

    Get by Id: Use this method to retrieve a ChartData object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
