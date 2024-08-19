from typing import List, Dict
from aiohttp import web

from openapi_server.models.runbook_list_by_automation_account_default_response import RunbookListByAutomationAccountDefaultResponse
from openapi_server.models.test_job_streams_list_by_test_job200_response import TestJobStreamsListByTestJob200Response
from openapi_server.models.test_job_streams_list_by_test_job200_response_value_inner import TestJobStreamsListByTestJob200ResponseValueInner
from openapi_server import util


async def test_job_streams_get(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, job_stream_id, api_version) -> web.Response:
    """test_job_streams_get

    Retrieve a test job stream of the test job identified by runbook name and stream id.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The runbook name.
    :type runbook_name: str
    :param job_stream_id: The job stream id.
    :type job_stream_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def test_job_streams_list_by_test_job(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version, filter=None) -> web.Response:
    """test_job_streams_list_by_test_job

    Retrieve a list of test job streams identified by runbook name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The runbook name.
    :type runbook_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)
