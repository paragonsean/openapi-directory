from typing import List, Dict
from aiohttp import web

from openapi_server.models.dsc_compilation_job import DscCompilationJob
from openapi_server.models.dsc_compilation_job_create_parameters import DscCompilationJobCreateParameters
from openapi_server.models.dsc_compilation_job_list_by_automation_account_default_response import DscCompilationJobListByAutomationAccountDefaultResponse
from openapi_server.models.dsc_compilation_job_list_result import DscCompilationJobListResult
from openapi_server.models.job_stream import JobStream
from openapi_server.models.job_stream_list_result import JobStreamListResult
from openapi_server import util


async def dsc_compilation_job_create(request: web.Request, resource_group_name, automation_account_name, compilation_job_name, subscription_id, api_version, parameters) -> web.Response:
    """dsc_compilation_job_create

    Creates the Dsc compilation job of the configuration.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param compilation_job_name: The DSC configuration Id.
    :type compilation_job_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the create compilation job operation.
    :type parameters: dict | bytes

    """
    parameters = DscCompilationJobCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def dsc_compilation_job_get(request: web.Request, resource_group_name, automation_account_name, compilation_job_name, subscription_id, api_version) -> web.Response:
    """dsc_compilation_job_get

    Retrieve the Dsc configuration compilation job identified by job id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param compilation_job_name: The DSC configuration Id.
    :type compilation_job_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dsc_compilation_job_get_stream(request: web.Request, resource_group_name, automation_account_name, job_id, job_stream_id, subscription_id, api_version) -> web.Response:
    """dsc_compilation_job_get_stream

    Retrieve the job stream identified by job stream id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_id: The job id.
    :type job_id: str
    :type job_id: str
    :param job_stream_id: The job stream id.
    :type job_stream_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dsc_compilation_job_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, filter=None) -> web.Response:
    """dsc_compilation_job_list_by_automation_account

    Retrieve a list of dsc compilation jobs.

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


async def dsc_compilation_job_stream_list_by_job(request: web.Request, resource_group_name, automation_account_name, job_id, subscription_id, api_version) -> web.Response:
    """dsc_compilation_job_stream_list_by_job

    Retrieve all the job streams for the compilation Job.

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
