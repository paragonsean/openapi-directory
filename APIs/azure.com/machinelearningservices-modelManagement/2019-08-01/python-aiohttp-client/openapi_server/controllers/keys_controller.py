from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_keys import AuthKeys
from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server.models.regenerate_service_keys_request import RegenerateServiceKeysRequest
from openapi_server import util


async def services_list_service_keys_0(request: web.Request, subscription_id, resource_group, workspace, id) -> web.Response:
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


async def services_regenerate_service_keys_0(request: web.Request, subscription_id, resource_group, workspace, id, request) -> web.Response:
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
