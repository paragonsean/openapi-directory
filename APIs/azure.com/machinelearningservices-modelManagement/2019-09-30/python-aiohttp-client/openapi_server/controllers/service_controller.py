from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_keys import AuthKeys
from openapi_server.models.auth_token import AuthToken
from openapi_server.models.create_service_request import CreateServiceRequest
from openapi_server.models.json_patch_operation import JsonPatchOperation
from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server.models.paginated_service_list import PaginatedServiceList
from openapi_server.models.regenerate_service_keys_request import RegenerateServiceKeysRequest
from openapi_server.models.service_response_base import ServiceResponseBase
from openapi_server import util


async def services_create(request: web.Request, subscription_id, resource_group, workspace, request) -> web.Response:
    """Create a Service.

    Create a Service with the specified payload.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param request: The payload that is used to create the Service.
    :type request: dict | bytes

    """
    request = CreateServiceRequest.from_dict(request)
    return web.Response(status=200)


async def services_delete(request: web.Request, subscription_id, resource_group, workspace, id) -> web.Response:
    """Delete a Service.

    Delete a specific Service.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The Service Id.
    :type id: str

    """
    return web.Response(status=200)


async def services_get_service_token(request: web.Request, subscription_id, resource_group, workspace, id) -> web.Response:
    """Generate Service Access Token.

    Gets access token that can be used for calling service.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The Service Id.
    :type id: str

    """
    return web.Response(status=200)


async def services_list_query(request: web.Request, subscription_id, resource_group, workspace, image_id=None, image_name=None, model_id=None, model_name=None, name=None, count=None, compute_type=None, skip_token=None, tags=None, properties=None, expand=None, orderby=None) -> web.Response:
    """Query the list of Services in a Workspace.

    If no filter is passed, the query lists all Services in the Workspace. The returned list is paginated and the count of item in each page is an optional parameter.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param image_id: The Image Id.
    :type image_id: str
    :param image_name: The Image name.
    :type image_name: str
    :param model_id: The Model Id.
    :type model_id: str
    :param model_name: The Model name.
    :type model_name: str
    :param name: The object name.
    :type name: str
    :param count: The number of items to retrieve in a page.
    :type count: int
    :param compute_type: The compute environment type.
    :type compute_type: str
    :param skip_token: The continuation token to retrieve the next page.
    :type skip_token: str
    :param tags: A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key&#x3D;value              Example: tagKey1,tagKey2,tagKey3&#x3D;value3
    :type tags: str
    :param properties: A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key&#x3D;value              Example: propKey1,propKey2,propKey3&#x3D;value3
    :type properties: str
    :param expand: Set to True to include Model details.
    :type expand: bool
    :param orderby: The option to order the response.
    :type orderby: str

    """
    return web.Response(status=200)


async def services_list_service_keys(request: web.Request, subscription_id, resource_group, workspace, id) -> web.Response:
    """Lists Service keys.

    Gets a list of Service keys.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The Service Id.
    :type id: str

    """
    return web.Response(status=200)


async def services_patch(request: web.Request, subscription_id, resource_group, workspace, id, patch) -> web.Response:
    """Patch a Service.

    Patch a specific Service.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The Service Id.
    :type id: str
    :param patch: The payload that is used to patch the Service.
    :type patch: list | bytes

    """
    patch = [JsonPatchOperation.from_dict(d) for d in patch]
    return web.Response(status=200)


async def services_query_by_id(request: web.Request, subscription_id, resource_group, workspace, id, expand=None) -> web.Response:
    """Get a Service.

    Get a Service by Id.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The Service Id.
    :type id: str
    :param expand: Set to True to include Model details.
    :type expand: bool

    """
    return web.Response(status=200)


async def services_regenerate_service_keys(request: web.Request, subscription_id, resource_group, workspace, id, request) -> web.Response:
    """Regenerate Service Keys.

    Regenerate and return the Service keys.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The Service Id.
    :type id: str
    :param request: The payload that is used to regenerate keys.
    :type request: dict | bytes

    """
    request = RegenerateServiceKeysRequest.from_dict(request)
    return web.Response(status=200)
