from typing import List, Dict
from aiohttp import web

from openapi_server.models.table_rows import TableRows
from openapi_server import util


async def tables_rows_get_id(request: web.Request, id) -> web.Response:
    """Rows: Get by Id

    Get by Id: Use this method to retrieve a Rows object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
