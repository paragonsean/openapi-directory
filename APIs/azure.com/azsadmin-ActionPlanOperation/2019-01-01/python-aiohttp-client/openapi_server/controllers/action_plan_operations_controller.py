from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_plan_operation_resource_entity import ActionPlanOperationResourceEntity
from openapi_server.models.action_plan_operations_list import ActionPlanOperationsList
from openapi_server import util


async def action_plan_operations_get(request: web.Request, subscription_id, plan_id, operation_id, api_version) -> web.Response:
    """action_plan_operations_get

    Gets the specified action plan operation

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param plan_id: Identifier of the action plan.
    :type plan_id: str
    :param operation_id: Identifier of the action plan operation.
    :type operation_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def action_plan_operations_list(request: web.Request, subscription_id, plan_id, api_version) -> web.Response:
    """action_plan_operations_list

    Lists the action plan operations

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param plan_id: Identifier of the action plan.
    :type plan_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
