from typing import List, Dict
from aiohttp import web

from openapi_server.models.hybrid_runbook_worker_group import HybridRunbookWorkerGroup
from openapi_server.models.hybrid_runbook_worker_group_list_by_automation_account_default_response import HybridRunbookWorkerGroupListByAutomationAccountDefaultResponse
from openapi_server.models.hybrid_runbook_worker_group_update_parameters import HybridRunbookWorkerGroupUpdateParameters
from openapi_server.models.hybrid_runbook_worker_groups_list_result import HybridRunbookWorkerGroupsListResult
from openapi_server import util


async def hybrid_runbook_worker_group_delete(request: web.Request, resource_group_name, automation_account_name, hybrid_runbook_worker_group_name, subscription_id, api_version) -> web.Response:
    """hybrid_runbook_worker_group_delete

    Delete a hybrid runbook worker group.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param hybrid_runbook_worker_group_name: The hybrid runbook worker group name
    :type hybrid_runbook_worker_group_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def hybrid_runbook_worker_group_get(request: web.Request, resource_group_name, automation_account_name, hybrid_runbook_worker_group_name, subscription_id, api_version) -> web.Response:
    """hybrid_runbook_worker_group_get

    Retrieve a hybrid runbook worker group.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param hybrid_runbook_worker_group_name: The hybrid runbook worker group name
    :type hybrid_runbook_worker_group_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def hybrid_runbook_worker_group_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, filter=None) -> web.Response:
    """hybrid_runbook_worker_group_list_by_automation_account

    Retrieve a list of hybrid runbook worker groups.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def hybrid_runbook_worker_group_update(request: web.Request, resource_group_name, automation_account_name, hybrid_runbook_worker_group_name, subscription_id, api_version, parameters) -> web.Response:
    """hybrid_runbook_worker_group_update

    Update a hybrid runbook worker group.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param hybrid_runbook_worker_group_name: The hybrid runbook worker group name
    :type hybrid_runbook_worker_group_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The hybrid runbook worker group
    :type parameters: dict | bytes

    """
    parameters = HybridRunbookWorkerGroupUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
