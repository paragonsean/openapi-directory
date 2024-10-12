from typing import List, Dict
from aiohttp import web

from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server.models.paginated_profile_response_list import PaginatedProfileResponseList
from openapi_server.models.profile_request_base import ProfileRequestBase
from openapi_server.models.profile_response import ProfileResponse
from openapi_server import util


async def profiles_create(request: web.Request, subscription_id, resource_group, workspace, image_id, input_request) -> web.Response:
    """Create a Profile.

    Create a Profile for an Image.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param image_id: The Image Id.
    :type image_id: str
    :param input_request: The payload that is used to create the Profile.
    :type input_request: dict | bytes

    """
    input_request = ProfileRequestBase.from_dict(input_request)
    return web.Response(status=200)


async def profiles_list_query(request: web.Request, subscription_id, resource_group, workspace, image_id, name=None, description=None, tags=None, properties=None, count=None, skip_token=None, order_by=None) -> web.Response:
    """Get a list of Image Profiles.

    If no filter is passed, the query lists all Profiles for the Image. The returned list is paginated and the count of items in each page is an optional parameter.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param image_id: The Image Id.
    :type image_id: str
    :param name: The Profile name.
    :type name: str
    :param description: The Profile description.
    :type description: str
    :param tags: A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key&#x3D;value              Example: tagKey1,tagKey2,tagKey3&#x3D;value3
    :type tags: str
    :param properties: A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key&#x3D;value              Example: propKey1,propKey2,propKey3&#x3D;value3
    :type properties: str
    :param count: The number of items to retrieve in a page.
    :type count: int
    :param skip_token: The continuation token to retrieve the next page.
    :type skip_token: str
    :param order_by: The option to order the response.
    :type order_by: str

    """
    return web.Response(status=200)


async def profiles_query_by_id(request: web.Request, subscription_id, resource_group, workspace, image_id, id) -> web.Response:
    """Get a Profile.

    Get the Profile for an Image.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param image_id: The Image Id.
    :type image_id: str
    :param id: The Profile Id.
    :type id: str

    """
    return web.Response(status=200)
