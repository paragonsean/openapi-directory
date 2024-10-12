from typing import List, Dict
from aiohttp import web

from openapi_server.models.software_update_configuration_run import SoftwareUpdateConfigurationRun
from openapi_server.models.software_update_configuration_run_list_result import SoftwareUpdateConfigurationRunListResult
from openapi_server.models.software_update_configuration_runs_list_default_response import SoftwareUpdateConfigurationRunsListDefaultResponse
from openapi_server import util


async def software_update_configuration_runs_get_by_id(request: web.Request, subscription_id, resource_group_name, automation_account_name, software_update_configuration_run_id, api_version, client_request_id=None) -> web.Response:
    """software_update_configuration_runs_get_by_id

    Get a single software update configuration Run by Id.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param software_update_configuration_run_id: The Id of the software update configuration run.
    :type software_update_configuration_run_id: str
    :type software_update_configuration_run_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str

    """
    return web.Response(status=200)


async def software_update_configuration_runs_list(request: web.Request, subscription_id, resource_group_name, automation_account_name, api_version, client_request_id=None, filter=None, skip=None, top=None) -> web.Response:
    """software_update_configuration_runs_list

    Return list of software update configuration runs

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str
    :param filter: The filter to apply on the operation. You can use the following filters: &#39;properties/osType&#39;, &#39;properties/status&#39;, &#39;properties/startTime&#39;, and &#39;properties/softwareUpdateConfiguration/name&#39;
    :type filter: str
    :param skip: Number of entries you skip before returning results
    :type skip: str
    :param top: Maximum number of entries returned in the results collection
    :type top: str

    """
    return web.Response(status=200)
