from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_extended import DeploymentExtended
from openapi_server.models.deployment_list_result import DeploymentListResult
from openapi_server.models.deployment_validate_result import DeploymentValidateResult
from openapi_server.models.template_hash_result import TemplateHashResult
from openapi_server import util


async def deployments_calculate_template_hash(request: web.Request, api_version, template) -> web.Response:
    """deployments_calculate_template_hash

    Calculate the hash of the given template.

    :param api_version: Client Api Version.
    :type api_version: str
    :param template: The template provided to calculate hash.
    :type template: 

    """
    return web.Response(status=200)


async def deployments_cancel(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_cancel

    Cancel a currently running template deployment.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_check_existence(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_check_existence

    Checks whether deployment exists.

    :param resource_group_name: The name of the resource group to check. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_create_or_update(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id, parameters) -> web.Response:
    """deployments_create_or_update

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


async def deployments_delete(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_delete

    Begin deleting deployment.To determine whether the operation has finished processing the request, call GetLongRunningOperationStatus.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment to be deleted.
    :type deployment_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_get(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_get

    Get a deployment.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_list(request: web.Request, resource_group_name, api_version, subscription_id, filter=None, top=None) -> web.Response:
    """deployments_list

    Get a list of deployments.

    :param resource_group_name: The name of the resource group to filter by. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: Query parameters. If null is passed returns all deployments.
    :type top: int

    """
    return web.Response(status=200)


async def deployments_validate(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id, parameters) -> web.Response:
    """deployments_validate

    Validate a deployment template.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Deployment to validate.
    :type parameters: dict | bytes

    """
    parameters = Deployment.from_dict(parameters)
    return web.Response(status=200)
