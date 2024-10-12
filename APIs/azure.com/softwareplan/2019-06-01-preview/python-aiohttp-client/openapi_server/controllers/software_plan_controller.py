from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server import util


async def software_plan_register(request: web.Request, subscription_id, api_version) -> web.Response:
    """software_plan_register

    Register to Microsoft.SoftwarePlan resource provider.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param api_version: The api-version to be used by the service
    :type api_version: str

    """
    return web.Response(status=200)
