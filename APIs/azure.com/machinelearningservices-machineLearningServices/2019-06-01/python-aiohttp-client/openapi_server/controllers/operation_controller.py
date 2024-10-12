from typing import List, Dict
from aiohttp import web

from openapi_server.models.machine_learning_service_error import MachineLearningServiceError
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists all of the available Azure Machine Learning Workspaces REST API operations.

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str

    """
    return web.Response(status=200)
