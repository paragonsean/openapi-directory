from typing import List, Dict
from aiohttp import web

from openapi_server.models.task_status_list import TaskStatusList
from openapi_server import util


async def task_status_get(request: web.Request, ) -> web.Response:
    """Gets list of Task Statuses

    


    """
    return web.Response(status=200)
