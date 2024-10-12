from typing import List, Dict
from aiohttp import web

from openapi_server.models.private_link_resource_list_result import PrivateLinkResourceListResult
from openapi_server import util


async def private_link_resources_list_by_workspace(request: web.Request, subscription_id, resource_group_name, workspace_name, api_version) -> web.Response:
    """private_link_resources_list_by_workspace

    Gets the private link resources that need to be created for a workspace.

    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str
    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str

    """
    return web.Response(status=200)
