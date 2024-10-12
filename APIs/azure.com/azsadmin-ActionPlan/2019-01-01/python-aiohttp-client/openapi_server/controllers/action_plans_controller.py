from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_plan_list import ActionPlanList
from openapi_server.models.action_plan_resource_entity import ActionPlanResourceEntity
from openapi_server import util


async def action_plans_get(request: web.Request, subscription_id, plan_id, api_version) -> web.Response:
    """action_plans_get

    Gets the specified action plan

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param plan_id: Identifier of the action plan.
    :type plan_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def action_plans_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """action_plans_list

    Gets the list of action plans

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
