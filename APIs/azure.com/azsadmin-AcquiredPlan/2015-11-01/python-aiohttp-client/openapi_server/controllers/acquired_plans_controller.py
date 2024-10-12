from typing import List, Dict
from aiohttp import web

from openapi_server.models.plan_acquisition import PlanAcquisition
from openapi_server.models.plan_acquisition_list import PlanAcquisitionList
from openapi_server import util


async def acquired_plans_create(request: web.Request, subscription_id, target_subscription_id, plan_acquisition_id, api_version, new_acquired_plan) -> web.Response:
    """acquired_plans_create

    Creates an acquired plan.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param target_subscription_id: The target subscription ID.
    :type target_subscription_id: str
    :param plan_acquisition_id: The plan acquisition Identifier
    :type plan_acquisition_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param new_acquired_plan: The new acquired plan.
    :type new_acquired_plan: dict | bytes

    """
    new_acquired_plan = PlanAcquisition.from_dict(new_acquired_plan)
    return web.Response(status=200)


async def acquired_plans_delete(request: web.Request, subscription_id, target_subscription_id, plan_acquisition_id, api_version) -> web.Response:
    """acquired_plans_delete

    Deletes an acquired plan.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param target_subscription_id: The target subscription ID.
    :type target_subscription_id: str
    :param plan_acquisition_id: The plan acquisition Identifier
    :type plan_acquisition_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def acquired_plans_get(request: web.Request, subscription_id, target_subscription_id, plan_acquisition_id, api_version) -> web.Response:
    """acquired_plans_get

    Gets the specified plan acquired by a subscription consuming the offer.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param target_subscription_id: The target subscription ID.
    :type target_subscription_id: str
    :param plan_acquisition_id: The plan acquisition Identifier
    :type plan_acquisition_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def acquired_plans_list(request: web.Request, subscription_id, target_subscription_id, api_version) -> web.Response:
    """acquired_plans_list

    Get a collection of all acquired plans that subscription has access to.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param target_subscription_id: The target subscription ID.
    :type target_subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
