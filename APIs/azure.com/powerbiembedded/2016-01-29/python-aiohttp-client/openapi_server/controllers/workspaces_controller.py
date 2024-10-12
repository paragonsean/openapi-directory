from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.workspace_list import WorkspaceList
from openapi_server import util


async def workspaces_list(request: web.Request, subscription_id, resource_group_name, workspace_collection_name, api_version) -> web.Response:
    """workspaces_list

    Retrieves all existing Power BI workspaces in the specified workspace collection.

    :param subscription_id: Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Azure resource group
    :type resource_group_name: str
    :param workspace_collection_name: Power BI Embedded Workspace Collection name
    :type workspace_collection_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
