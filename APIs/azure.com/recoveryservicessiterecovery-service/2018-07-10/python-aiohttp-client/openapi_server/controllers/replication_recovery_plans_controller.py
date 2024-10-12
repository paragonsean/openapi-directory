from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_recovery_plan_input import CreateRecoveryPlanInput
from openapi_server.models.recovery_plan import RecoveryPlan
from openapi_server.models.recovery_plan_collection import RecoveryPlanCollection
from openapi_server.models.recovery_plan_planned_failover_input import RecoveryPlanPlannedFailoverInput
from openapi_server.models.recovery_plan_test_failover_cleanup_input import RecoveryPlanTestFailoverCleanupInput
from openapi_server.models.recovery_plan_test_failover_input import RecoveryPlanTestFailoverInput
from openapi_server.models.recovery_plan_unplanned_failover_input import RecoveryPlanUnplannedFailoverInput
from openapi_server.models.update_recovery_plan_input import UpdateRecoveryPlanInput
from openapi_server import util


async def replication_recovery_plans_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, recovery_plan_name, input) -> web.Response:
    """Creates a recovery plan with the given details.

    The operation to create a recovery plan.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param recovery_plan_name: Recovery plan name.
    :type recovery_plan_name: str
    :param input: Recovery Plan creation input.
    :type input: dict | bytes

    """
    input = CreateRecoveryPlanInput.from_dict(input)
    return web.Response(status=200)


async def replication_recovery_plans_delete(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, recovery_plan_name) -> web.Response:
    """Deletes the specified recovery plan.

    Delete a recovery plan.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param recovery_plan_name: Recovery plan name.
    :type recovery_plan_name: str

    """
    return web.Response(status=200)


async def replication_recovery_plans_failover_commit(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, recovery_plan_name) -> web.Response:
    """Execute commit failover of the recovery plan.

    The operation to commit the fail over of a recovery plan.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param recovery_plan_name: Recovery plan name.
    :type recovery_plan_name: str

    """
    return web.Response(status=200)


async def replication_recovery_plans_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, recovery_plan_name) -> web.Response:
    """Gets the requested recovery plan.

    Gets the details of the recovery plan.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param recovery_plan_name: Name of the recovery plan.
    :type recovery_plan_name: str

    """
    return web.Response(status=200)


async def replication_recovery_plans_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the list of recovery plans.

    Lists the recovery plans in the vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def replication_recovery_plans_planned_failover(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, recovery_plan_name, input) -> web.Response:
    """Execute planned failover of the recovery plan.

    The operation to start the planned failover of a recovery plan.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param recovery_plan_name: Recovery plan name.
    :type recovery_plan_name: str
    :param input: Failover input.
    :type input: dict | bytes

    """
    input = RecoveryPlanPlannedFailoverInput.from_dict(input)
    return web.Response(status=200)


async def replication_recovery_plans_reprotect(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, recovery_plan_name) -> web.Response:
    """Execute reprotect of the recovery plan.

    The operation to reprotect(reverse replicate) a recovery plan.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param recovery_plan_name: Recovery plan name.
    :type recovery_plan_name: str

    """
    return web.Response(status=200)


async def replication_recovery_plans_test_failover(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, recovery_plan_name, input) -> web.Response:
    """Execute test failover of the recovery plan.

    The operation to start the test failover of a recovery plan.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param recovery_plan_name: Recovery plan name.
    :type recovery_plan_name: str
    :param input: Failover input.
    :type input: dict | bytes

    """
    input = RecoveryPlanTestFailoverInput.from_dict(input)
    return web.Response(status=200)


async def replication_recovery_plans_test_failover_cleanup(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, recovery_plan_name, input) -> web.Response:
    """Execute test failover cleanup of the recovery plan.

    The operation to cleanup test failover of a recovery plan.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param recovery_plan_name: Recovery plan name.
    :type recovery_plan_name: str
    :param input: Test failover cleanup input.
    :type input: dict | bytes

    """
    input = RecoveryPlanTestFailoverCleanupInput.from_dict(input)
    return web.Response(status=200)


async def replication_recovery_plans_unplanned_failover(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, recovery_plan_name, input) -> web.Response:
    """Execute unplanned failover of the recovery plan.

    The operation to start the failover of a recovery plan.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param recovery_plan_name: Recovery plan name.
    :type recovery_plan_name: str
    :param input: Failover input.
    :type input: dict | bytes

    """
    input = RecoveryPlanUnplannedFailoverInput.from_dict(input)
    return web.Response(status=200)


async def replication_recovery_plans_update(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, recovery_plan_name, input) -> web.Response:
    """Updates the given recovery plan.

    The operation to update a recovery plan.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param recovery_plan_name: Recovery plan name.
    :type recovery_plan_name: str
    :param input: Update recovery plan input
    :type input: dict | bytes

    """
    input = UpdateRecoveryPlanInput.from_dict(input)
    return web.Response(status=200)
