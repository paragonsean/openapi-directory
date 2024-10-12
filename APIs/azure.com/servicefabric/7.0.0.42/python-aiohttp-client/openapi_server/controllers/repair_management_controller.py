from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.repair_task import RepairTask
from openapi_server.models.repair_task_approve_description import RepairTaskApproveDescription
from openapi_server.models.repair_task_cancel_description import RepairTaskCancelDescription
from openapi_server.models.repair_task_delete_description import RepairTaskDeleteDescription
from openapi_server.models.repair_task_update_health_policy_description import RepairTaskUpdateHealthPolicyDescription
from openapi_server.models.repair_task_update_info import RepairTaskUpdateInfo
from openapi_server import util


async def cancel_repair_task(request: web.Request, api_version, repair_task_cancel_description) -> web.Response:
    """Requests the cancellation of the given repair task.

    This API supports the Service Fabric platform; it is not meant to be used directly from your code.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param repair_task_cancel_description: Describes the repair task to be cancelled.
    :type repair_task_cancel_description: dict | bytes

    """
    repair_task_cancel_description = RepairTaskCancelDescription.from_dict(repair_task_cancel_description)
    return web.Response(status=200)


async def create_repair_task(request: web.Request, api_version, repair_task) -> web.Response:
    """Creates a new repair task.

    For clusters that have the Repair Manager Service configured, this API provides a way to create repair tasks that run automatically or manually. For repair tasks that run automatically, an appropriate repair executor must be running for each repair action to run automatically. These are currently only available in specially-configured Azure Cloud Services.  To create a manual repair task, provide the set of impacted node names and the expected impact. When the state of the created repair task changes to approved, you can safely perform repair actions on those nodes.  This API supports the Service Fabric platform; it is not meant to be used directly from your code.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param repair_task: Describes the repair task to be created or updated.
    :type repair_task: dict | bytes

    """
    repair_task = RepairTask.from_dict(repair_task)
    return web.Response(status=200)


async def delete_repair_task(request: web.Request, api_version, repair_task_delete_description) -> web.Response:
    """Deletes a completed repair task.

    This API supports the Service Fabric platform; it is not meant to be used directly from your code.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param repair_task_delete_description: Describes the repair task to be deleted.
    :type repair_task_delete_description: dict | bytes

    """
    repair_task_delete_description = RepairTaskDeleteDescription.from_dict(repair_task_delete_description)
    return web.Response(status=200)


async def force_approve_repair_task(request: web.Request, api_version, repair_task_approve_description) -> web.Response:
    """Forces the approval of the given repair task.

    This API supports the Service Fabric platform; it is not meant to be used directly from your code.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param repair_task_approve_description: Describes the repair task to be approved.
    :type repair_task_approve_description: dict | bytes

    """
    repair_task_approve_description = RepairTaskApproveDescription.from_dict(repair_task_approve_description)
    return web.Response(status=200)


async def get_repair_task_list(request: web.Request, api_version, task_id_filter=None, state_filter=None, executor_filter=None) -> web.Response:
    """Gets a list of repair tasks matching the given filters.

    This API supports the Service Fabric platform; it is not meant to be used directly from your code.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param task_id_filter: The repair task ID prefix to be matched.
    :type task_id_filter: str
    :param state_filter: A bitwise-OR of the following values, specifying which task states should be included in the result list.  - 1 - Created - 2 - Claimed - 4 - Preparing - 8 - Approved - 16 - Executing - 32 - Restoring - 64 - Completed
    :type state_filter: int
    :param executor_filter: The name of the repair executor whose claimed tasks should be included in the list.
    :type executor_filter: str

    """
    return web.Response(status=200)


async def update_repair_execution_state(request: web.Request, api_version, repair_task) -> web.Response:
    """Updates the execution state of a repair task.

    This API supports the Service Fabric platform; it is not meant to be used directly from your code.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param repair_task: Describes the repair task to be created or updated.
    :type repair_task: dict | bytes

    """
    repair_task = RepairTask.from_dict(repair_task)
    return web.Response(status=200)


async def update_repair_task_health_policy(request: web.Request, api_version, repair_task_update_health_policy_description) -> web.Response:
    """Updates the health policy of the given repair task.

    This API supports the Service Fabric platform; it is not meant to be used directly from your code.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param repair_task_update_health_policy_description: Describes the repair task healthy policy to be updated.
    :type repair_task_update_health_policy_description: dict | bytes

    """
    repair_task_update_health_policy_description = RepairTaskUpdateHealthPolicyDescription.from_dict(repair_task_update_health_policy_description)
    return web.Response(status=200)
