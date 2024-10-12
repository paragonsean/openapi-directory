from typing import List, Dict
from aiohttp import web

from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_extended import DeploymentExtended
from openapi_server import util


async def virtual_machines_quick_create(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id, parameters=None) -> web.Response:
    """virtual_machines_quick_create

    Create a named template deployment using a template.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Additional parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = Deployment.from_dict(parameters)
    return web.Response(status=200)
