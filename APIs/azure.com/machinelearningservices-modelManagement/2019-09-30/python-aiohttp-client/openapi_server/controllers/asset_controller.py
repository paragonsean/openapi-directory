from typing import List, Dict
from aiohttp import web

from openapi_server.models.asset import Asset
from openapi_server.models.json_patch_operation import JsonPatchOperation
from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server.models.paginated_asset_list import PaginatedAssetList
from openapi_server import util


async def assets_create(request: web.Request, subscription_id, resource_group, workspace, asset=None) -> web.Response:
    """Create an Asset.

    Create an Asset from the provided payload.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param asset: The Asset to be created.
    :type asset: dict | bytes

    """
    asset = Asset.from_dict(asset)
    return web.Response(status=200)


async def assets_delete(request: web.Request, subscription_id, resource_group, workspace, id) -> web.Response:
    """Delete an Asset.

    Delete the specified Asset.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The Id of the Asset to delete.
    :type id: str

    """
    return web.Response(status=200)


async def assets_list_query(request: web.Request, subscription_id, resource_group, workspace, run_id=None, name=None, count=None, skip_token=None, tags=None, properties=None, orderby=None) -> web.Response:
    """Query the list of Assets in a workspace.

    If no filter is passed, the query lists all the Assets in the given workspace. The returned list is paginated and the count of items in each page is an optional parameter.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param run_id: The run Id associated with the Assets.
    :type run_id: str
    :param name: The object name.
    :type name: str
    :param count: The number of items to retrieve in a page.
    :type count: int
    :param skip_token: The continuation token to retrieve the next page.
    :type skip_token: str
    :param tags: A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key&#x3D;value              Example: tagKey1,tagKey2,tagKey3&#x3D;value3
    :type tags: str
    :param properties: A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key&#x3D;value              Example: propKey1,propKey2,propKey3&#x3D;value3
    :type properties: str
    :param orderby: An option for specifying how to order the list.
    :type orderby: str

    """
    return web.Response(status=200)


async def assets_patch(request: web.Request, subscription_id, resource_group, workspace, id, patch) -> web.Response:
    """Update an Asset.

    Patch a specific Asset.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The Id of the Asset to patch.
    :type id: str
    :param patch: The payload that is used to patch an Asset.
    :type patch: list | bytes

    """
    patch = [JsonPatchOperation.from_dict(d) for d in patch]
    return web.Response(status=200)


async def assets_query_by_id(request: web.Request, subscription_id, resource_group, workspace, id) -> web.Response:
    """Get an Asset.

    Get an Asset by Id.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The Asset Id.
    :type id: str

    """
    return web.Response(status=200)
