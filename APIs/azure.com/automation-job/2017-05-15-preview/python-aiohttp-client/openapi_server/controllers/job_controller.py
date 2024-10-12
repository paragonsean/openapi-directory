from typing import List, Dict
from aiohttp import web

from openapi_server.models.job import Job
from openapi_server.models.job_create_parameters import JobCreateParameters
from openapi_server.models.job_list_by_automation_account_default_response import JobListByAutomationAccountDefaultResponse
from openapi_server.models.job_list_result_v2 import JobListResultV2
from openapi_server import util


async def job_create(request: web.Request, subscription_id, resource_group_name, automation_account_name, job_name, api_version, parameters, client_request_id=None) -> web.Response:
    """job_create

    Create a job of the runbook.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_name: The job name.
    :type job_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the create job operation.
    :type parameters: dict | bytes
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str

    """
    parameters = JobCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def job_get(request: web.Request, subscription_id, resource_group_name, automation_account_name, job_name, api_version, client_request_id=None) -> web.Response:
    """job_get

    Retrieve the job identified by job name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_name: The job name.
    :type job_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str

    """
    return web.Response(status=200)


async def job_get_output(request: web.Request, subscription_id, resource_group_name, automation_account_name, job_name, api_version, client_request_id=None) -> web.Response:
    """job_get_output

    Retrieve the job output identified by job name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_name: The name of the job to be created.
    :type job_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str

    """
    return web.Response(status=200)


async def job_get_runbook_content(request: web.Request, subscription_id, resource_group_name, automation_account_name, job_name, api_version, client_request_id=None) -> web.Response:
    """job_get_runbook_content

    Retrieve the runbook content of the job identified by job name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_name: The job name.
    :type job_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str

    """
    return web.Response(status=200)


async def job_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, filter=None, client_request_id=None) -> web.Response:
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
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str

    """
    return web.Response(status=200)


async def job_resume(request: web.Request, resource_group_name, automation_account_name, job_name, subscription_id, api_version, client_request_id=None) -> web.Response:
    """job_resume

    Resume the job identified by jobName.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_name: The job name.
    :type job_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str

    """
    return web.Response(status=200)


async def job_stop(request: web.Request, resource_group_name, automation_account_name, job_name, subscription_id, api_version, client_request_id=None) -> web.Response:
    """job_stop

    Stop the job identified by jobName.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_name: The job name.
    :type job_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str

    """
    return web.Response(status=200)


async def job_suspend(request: web.Request, subscription_id, resource_group_name, automation_account_name, job_name, api_version, client_request_id=None) -> web.Response:
    """job_suspend

    Suspend the job identified by job name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_name: The job name.
    :type job_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str

    """
    return web.Response(status=200)
