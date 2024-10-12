from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.trigger_resource import TriggerResource
from openapi_server import util


async def triggers_get(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, api_version) -> web.Response:
    """triggers_get

    Gets a trigger.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
