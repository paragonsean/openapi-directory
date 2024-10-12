from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.get_task_response import GetTaskResponse
from openapi_server import util


async def get_task(request: web.Request, id) -> web.Response:
    """Get status of a task

    Gets status of a task 

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
