from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_token import AuthToken
from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server import util


async def services_get_service_token_0(request: web.Request, subscription_id, resource_group, workspace, id) -> web.Response:
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
