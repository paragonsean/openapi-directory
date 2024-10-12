from typing import List, Dict
from aiohttp import web

from openapi_server.models.available_operations import AvailableOperations
from openapi_server import util


async def machine_learning_compute_list_available_operations(request: web.Request, api_version) -> web.Response:
    """machine_learning_compute_list_available_operations

    Gets all available operations.

    :param api_version: The version of the Microsoft.MachineLearningCompute resource provider API to use.
    :type api_version: str

    """
    return web.Response(status=200)
