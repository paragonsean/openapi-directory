from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.operation_list import OperationList
from openapi_server import util


async def operations_list(request: web.Request, scope, api_version) -> web.Response:
    """Get operations.

    List all the operations.

    :param scope: The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    :type scope: str
    :param api_version: The api-version to be used by the service
    :type api_version: str

    """
    return web.Response(status=200)
