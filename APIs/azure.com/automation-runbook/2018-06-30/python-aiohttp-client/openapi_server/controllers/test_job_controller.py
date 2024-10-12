from typing import List, Dict
from aiohttp import web

from openapi_server.models.runbook_list_by_automation_account_default_response import RunbookListByAutomationAccountDefaultResponse
from openapi_server.models.test_job import TestJob
from openapi_server.models.test_job_create_parameters import TestJobCreateParameters
from openapi_server import util


async def test_job_create(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version, parameters) -> web.Response:
    """test_job_create

    Create a test job of the runbook.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The parameters supplied to the create test job operation.
    :type runbook_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the create test job operation.
    :type parameters: dict | bytes

    """
    parameters = TestJobCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def test_job_get(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version) -> web.Response:
    """test_job_get

    Retrieve the test job for the specified runbook.

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

    """
    return web.Response(status=200)


async def test_job_resume(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version) -> web.Response:
    """test_job_resume

    Resume the test job.

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

    """
    return web.Response(status=200)


async def test_job_stop(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version) -> web.Response:
    """test_job_stop

    Stop the test job.

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

    """
    return web.Response(status=200)


async def test_job_suspend(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version) -> web.Response:
    """test_job_suspend

    Suspend the test job.

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

    """
    return web.Response(status=200)
