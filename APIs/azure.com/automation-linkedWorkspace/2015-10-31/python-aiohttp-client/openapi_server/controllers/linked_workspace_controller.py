from typing import List, Dict
from aiohttp import web

from openapi_server.models.linked_workspace import LinkedWorkspace
from openapi_server.models.linked_workspace_get_default_response import LinkedWorkspaceGetDefaultResponse
from openapi_server import util


async def linked_workspace_get(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version) -> web.Response:
    """linked_workspace_get

    Retrieve the linked workspace for the account id.

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
