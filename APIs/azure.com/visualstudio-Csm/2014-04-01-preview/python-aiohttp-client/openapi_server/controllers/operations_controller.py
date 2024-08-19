from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_list_result import OperationListResult
from openapi_server import util


async def operations_list(request: web.Request, ) -> web.Response:
    """Operations_List

    Gets the details of all operations possible on the Microsoft.VisualStudio resource provider.


    """
    return web.Response(status=200)
