from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation import Operation
from openapi_server import util


async def get_operation(request: web.Request, operation_id) -> web.Response:
    """Get operation status

    Track progress of a long-running operation using the operations identifier returned when you  created the operation. For example, by triggering the analysis of a commit, or the code review of a patch. For both LGTM.com and LGTM Enterprise, you must include an access token with the &#x60;operations:read&#x60; scope. 

    :param operation_id: The operation identifier returned on creating the task.
    :type operation_id: int

    """
    return web.Response(status=200)
