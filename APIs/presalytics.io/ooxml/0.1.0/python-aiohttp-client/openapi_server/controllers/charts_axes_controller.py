from typing import List, Dict
from aiohttp import web

from openapi_server.models.chart_axes import ChartAxes
from openapi_server import util


async def chart_axes_get_id(request: web.Request, id) -> web.Response:
    """Axes: Get by Id

    Get by Id: Use this method to retrieve a Axes object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
