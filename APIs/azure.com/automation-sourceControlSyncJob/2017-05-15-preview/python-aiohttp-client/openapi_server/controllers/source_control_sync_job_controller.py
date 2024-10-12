from typing import List, Dict
from aiohttp import web

from openapi_server.models.source_control_sync_job import SourceControlSyncJob
from openapi_server.models.source_control_sync_job_by_id import SourceControlSyncJobById
from openapi_server.models.source_control_sync_job_create_parameters import SourceControlSyncJobCreateParameters
from openapi_server.models.source_control_sync_job_list_by_automation_account_default_response import SourceControlSyncJobListByAutomationAccountDefaultResponse
from openapi_server.models.source_control_sync_job_list_result import SourceControlSyncJobListResult
from openapi_server import util


async def source_control_sync_job_create(request: web.Request, resource_group_name, automation_account_name, source_control_name, source_control_sync_job_id, subscription_id, api_version, parameters) -> web.Response:
    """source_control_sync_job_create

    Creates the sync job for a source control.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param source_control_name: The source control name.
    :type source_control_name: str
    :param source_control_sync_job_id: The source control sync job id.
    :type source_control_sync_job_id: str
    :type source_control_sync_job_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the create source control sync job operation.
    :type parameters: dict | bytes

    """
    parameters = SourceControlSyncJobCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def source_control_sync_job_get(request: web.Request, resource_group_name, automation_account_name, source_control_name, source_control_sync_job_id, subscription_id, api_version) -> web.Response:
    """source_control_sync_job_get

    Retrieve the source control sync job identified by job id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param source_control_name: The source control name.
    :type source_control_name: str
    :param source_control_sync_job_id: The source control sync job id.
    :type source_control_sync_job_id: str
    :type source_control_sync_job_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def source_control_sync_job_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, source_control_name, subscription_id, api_version, filter=None) -> web.Response:
    """source_control_sync_job_list_by_automation_account

    Retrieve a list of source control sync jobs.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param source_control_name: The source control name.
    :type source_control_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)
