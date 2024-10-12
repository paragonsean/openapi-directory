from typing import List, Dict
from aiohttp import web

from openapi_server.models.machine_learning_service_error import MachineLearningServiceError
from openapi_server.models.sku_list_result import SkuListResult
from openapi_server import util


async def list_skus(request: web.Request, api_version, subscription_id) -> web.Response:
    """list_skus

    Lists all skus with associated features

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str

    """
    return web.Response(status=200)
