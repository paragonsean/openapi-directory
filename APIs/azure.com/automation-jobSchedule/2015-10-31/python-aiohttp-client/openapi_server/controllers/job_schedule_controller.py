from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_schedule import JobSchedule
from openapi_server.models.job_schedule_create_parameters import JobScheduleCreateParameters
from openapi_server.models.job_schedule_list_by_automation_account_default_response import JobScheduleListByAutomationAccountDefaultResponse
from openapi_server.models.job_schedule_list_result import JobScheduleListResult
from openapi_server import util


async def job_schedule_create(request: web.Request, resource_group_name, automation_account_name, job_schedule_id, subscription_id, api_version, parameters) -> web.Response:
    """job_schedule_create

    Create a job schedule.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_schedule_id: The job schedule name.
    :type job_schedule_id: str
    :type job_schedule_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the create job schedule operation.
    :type parameters: dict | bytes

    """
    parameters = JobScheduleCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def job_schedule_delete(request: web.Request, resource_group_name, automation_account_name, job_schedule_id, subscription_id, api_version) -> web.Response:
    """job_schedule_delete

    Delete the job schedule identified by job schedule name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_schedule_id: The job schedule name.
    :type job_schedule_id: str
    :type job_schedule_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_schedule_get(request: web.Request, resource_group_name, automation_account_name, job_schedule_id, subscription_id, api_version) -> web.Response:
    """job_schedule_get

    Retrieve the job schedule identified by job schedule name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_schedule_id: The job schedule name.
    :type job_schedule_id: str
    :type job_schedule_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_schedule_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, filter=None) -> web.Response:
    """job_schedule_list_by_automation_account

    Retrieve a list of job schedules.

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
