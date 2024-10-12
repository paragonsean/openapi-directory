from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.usage_models_result import UsageModelsResult
from openapi_server import util


async def usage_models_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """usage_models_list

    Get the list of Cache Usage Models available to this subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
