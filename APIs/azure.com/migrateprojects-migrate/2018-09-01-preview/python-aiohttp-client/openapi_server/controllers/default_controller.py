from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_result_list import OperationResultList
from openapi_server import util


async def operations_list(request: web.Request, ) -> web.Response:
    """Get list of operations supported in the API.

    Get a list of REST API supported by Microsoft.Migrate provider.


    """
    return web.Response(status=200)
