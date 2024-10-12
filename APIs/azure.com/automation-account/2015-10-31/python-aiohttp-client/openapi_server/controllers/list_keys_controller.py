from typing import List, Dict
from aiohttp import web

from openapi_server.models.key_list_result import KeyListResult
from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server import util


async def keys_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version) -> web.Response:
    """keys_list_by_automation_account

    Retrieve the automation keys for an account.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
