from typing import List, Dict
from aiohttp import web

from openapi_server.models.table_cells import TableCells
from openapi_server import util


async def tables_cells_get_id(request: web.Request, id) -> web.Response:
    """Cells: Get by Id

    Get by Id: Use this method to retrieve a Cells object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
