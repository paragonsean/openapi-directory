from typing import List, Dict
from aiohttp import web

from openapi_server.models.task_type_list import TaskTypeList
from openapi_server import util


async def task_type_get(request: web.Request, ) -> web.Response:
    """Gets list of Task Types

    


    """
    return web.Response(status=200)
