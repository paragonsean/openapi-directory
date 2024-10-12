from typing import List, Dict
from aiohttp import web

from openapi_server.models.job import Job
from openapi_server.models.job_create_parameters import JobCreateParameters
from openapi_server.models.job_list_by_automation_account_default_response import JobListByAutomationAccountDefaultResponse
from openapi_server.models.job_list_result import JobListResult
from openapi_server import util


async def job_create(request: web.Request, resource_group_name, automation_account_name, job_id, subscription_id, api_version, parameters) -> web.Response:
    """job_create

    Create a job of the runbook.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_id: The job id.
    :type job_id: str
    :type job_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the create job operation.
    :type parameters: dict | bytes

    """
    parameters = JobCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def job_get(request: web.Request, resource_group_name, automation_account_name, job_id, subscription_id, api_version) -> web.Response:
    """job_get

    Retrieve the job identified by job id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_id: The job id.
    :type job_id: str
    :type job_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_get_output(request: web.Request, resource_group_name, automation_account_name, job_id, subscription_id, api_version) -> web.Response:
    """job_get_output

    Retrieve the job output identified by job id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_id: The job id.
    :type job_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_get_runbook_content(request: web.Request, resource_group_name, automation_account_name, job_id, subscription_id, api_version) -> web.Response:
    """job_get_runbook_content

    Retrieve the runbook content of the job identified by job id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_id: The job id.
    :type job_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, filter=None) -> web.Response:
    """job_list_by_automation_account

    Retrieve a list of jobs.

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


async def job_resume(request: web.Request, resource_group_name, automation_account_name, job_id, subscription_id, api_version) -> web.Response:
    """job_resume

    Resume the job identified by jobId.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_id: The job id.
    :type job_id: str
    :type job_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_stop(request: web.Request, resource_group_name, automation_account_name, job_id, subscription_id, api_version) -> web.Response:
    """job_stop

    Stop the job identified by jobId.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_id: The job id.
    :type job_id: str
    :type job_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_suspend(request: web.Request, resource_group_name, automation_account_name, job_id, subscription_id, api_version) -> web.Response:
    """job_suspend

    Suspend the job identified by jobId.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_id: The job id.
    :type job_id: str
    :type job_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
