from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_list_by_automation_account_default_response import JobListByAutomationAccountDefaultResponse
from openapi_server.models.job_stream import JobStream
from openapi_server.models.job_stream_list_result import JobStreamListResult
from openapi_server import util


async def job_stream_get(request: web.Request, resource_group_name, automation_account_name, job_id, job_stream_id, subscription_id, api_version) -> web.Response:
    """job_stream_get

    Retrieve the job stream identified by job stream id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_id: The job id.
    :type job_id: str
    :param job_stream_id: The job stream id.
    :type job_stream_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_stream_list_by_job(request: web.Request, resource_group_name, automation_account_name, job_id, subscription_id, api_version, filter=None) -> web.Response:
    """job_stream_list_by_job

    Retrieve a list of jobs streams identified by job id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param job_id: The job Id.
    :type job_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)
