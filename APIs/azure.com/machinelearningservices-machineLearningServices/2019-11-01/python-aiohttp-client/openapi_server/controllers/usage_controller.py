from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_usages_result import ListUsagesResult
from openapi_server import util


async def usages_list(request: web.Request, api_version, subscription_id, location) -> web.Response:
    """usages_list

    Gets the current usage information as well as limits for AML resources for given subscription and location.

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param location: The location for which resource usage is queried.
    :type location: str

    """
    return web.Response(status=200)
