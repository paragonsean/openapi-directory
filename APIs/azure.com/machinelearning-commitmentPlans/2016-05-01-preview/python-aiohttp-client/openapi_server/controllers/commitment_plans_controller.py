from typing import List, Dict
from aiohttp import web

from openapi_server.models.commitment_plan import CommitmentPlan
from openapi_server.models.commitment_plan_list_result import CommitmentPlanListResult
from openapi_server.models.commitment_plan_patch_payload import CommitmentPlanPatchPayload
from openapi_server.models.plan_usage_history_list_result import PlanUsageHistoryListResult
from openapi_server import util


async def commitment_plans_create_or_update(request: web.Request, subscription_id, resource_group_name, commitment_plan_name, api_version, create_or_update_payload) -> web.Response:
    """commitment_plans_create_or_update

    Create a new Azure ML commitment plan resource or updates an existing one.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param commitment_plan_name: The Azure ML commitment plan name.
    :type commitment_plan_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param create_or_update_payload: The payload to create or update the Azure ML commitment plan.
    :type create_or_update_payload: dict | bytes

    """
    create_or_update_payload = CommitmentPlan.from_dict(create_or_update_payload)
    return web.Response(status=200)


async def commitment_plans_get(request: web.Request, subscription_id, resource_group_name, commitment_plan_name, api_version) -> web.Response:
    """commitment_plans_get

    Retrieve an Azure ML commitment plan by its subscription, resource group and name.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param commitment_plan_name: The Azure ML commitment plan name.
    :type commitment_plan_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def commitment_plans_list(request: web.Request, subscription_id, api_version, skip_token=None) -> web.Response:
    """commitment_plans_list

    Retrieve all Azure ML commitment plans in a subscription.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param skip_token: Continuation token for pagination.
    :type skip_token: str

    """
    return web.Response(status=200)


async def commitment_plans_list_in_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, skip_token=None) -> web.Response:
    """commitment_plans_list_in_resource_group

    Retrieve all Azure ML commitment plans in a resource group.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param skip_token: Continuation token for pagination.
    :type skip_token: str

    """
    return web.Response(status=200)


async def commitment_plans_patch(request: web.Request, subscription_id, resource_group_name, commitment_plan_name, api_version, patch_payload) -> web.Response:
    """commitment_plans_patch

    Patch an existing Azure ML commitment plan resource.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param commitment_plan_name: The Azure ML commitment plan name.
    :type commitment_plan_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param patch_payload: The payload to use to patch the Azure ML commitment plan. Only tags and SKU may be modified on an existing commitment plan.
    :type patch_payload: dict | bytes

    """
    patch_payload = CommitmentPlanPatchPayload.from_dict(patch_payload)
    return web.Response(status=200)


async def commitment_plans_remove(request: web.Request, subscription_id, resource_group_name, commitment_plan_name, api_version) -> web.Response:
    """commitment_plans_remove

    Remove an existing Azure ML commitment plan.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param commitment_plan_name: The Azure ML commitment plan name.
    :type commitment_plan_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def usage_history_list(request: web.Request, subscription_id, resource_group_name, commitment_plan_name, api_version, skip_token=None) -> web.Response:
    """usage_history_list

    Retrieve the usage history for an Azure ML commitment plan.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param commitment_plan_name: The Azure ML commitment plan name.
    :type commitment_plan_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param skip_token: Continuation token for pagination.
    :type skip_token: str

    """
    return web.Response(status=200)
