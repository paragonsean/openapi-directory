from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def farms_get_garbage_collection_state(request: web.Request, subscription_id, resource_group_name, farm_id, api_version, operation_id) -> web.Response:
    """farms_get_garbage_collection_state

    Returns the state of the garbage collection job.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param api_version: REST Api Version.
    :type api_version: str
    :param operation_id: Operation Id.
    :type operation_id: str

    """
    return web.Response(status=200)
