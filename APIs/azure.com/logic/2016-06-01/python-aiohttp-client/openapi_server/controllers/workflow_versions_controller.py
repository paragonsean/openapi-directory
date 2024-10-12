from typing import List, Dict
from aiohttp import web

from openapi_server.models.workflow_version import WorkflowVersion
from openapi_server.models.workflow_version_list_result import WorkflowVersionListResult
from openapi_server import util


async def workflow_versions_get(request: web.Request, subscription_id, resource_group_name, workflow_name, version_id, api_version) -> web.Response:
    """workflow_versions_get

    Gets a workflow version.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param version_id: The workflow versionId.
    :type version_id: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workflow_versions_list(request: web.Request, subscription_id, resource_group_name, workflow_name, api_version, top=None) -> web.Response:
    """workflow_versions_list

    Gets a list of workflow versions.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param workflow_name: The workflow name.
    :type workflow_name: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int

    """
    return web.Response(status=200)
