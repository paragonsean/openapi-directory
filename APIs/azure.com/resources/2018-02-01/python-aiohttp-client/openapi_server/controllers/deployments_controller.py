from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_export_result import DeploymentExportResult
from openapi_server.models.deployment_extended import DeploymentExtended
from openapi_server.models.deployment_list_result import DeploymentListResult
from openapi_server.models.deployment_validate_result import DeploymentValidateResult
from openapi_server.models.template_hash_result import TemplateHashResult
from openapi_server import util


async def deployments_calculate_template_hash(request: web.Request, api_version, template) -> web.Response:
    """deployments_calculate_template_hash

    Calculate the hash of the given template.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param template: The template provided to calculate hash.
    :type template: 

    """
    return web.Response(status=200)


async def deployments_cancel(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """Cancels a currently running template deployment.

    You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resource group partially deployed.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment to cancel.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_check_existence(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_check_existence

    Checks whether the deployment exists.

    :param resource_group_name: The name of the resource group with the deployment to check. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment to check.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_create_or_update(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id, parameters) -> web.Response:
    """Deploys resources to a resource group.

    You can provide the template and parameters directly in the request or link to JSON files.

    :param resource_group_name: The name of the resource group to deploy the resources to. The name is case insensitive. The resource group must already exist.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Additional parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = Deployment.from_dict(parameters)
    return web.Response(status=200)


async def deployments_delete(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """Deletes a deployment from the deployment history.

    A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. Deleting a template deployment does not affect the state of the resource group. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

    :param resource_group_name: The name of the resource group with the deployment to delete. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment to delete.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_export_template(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_export_template

    Exports the template used for specified deployment.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment from which to get the template.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_get(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_get

    Gets a deployment.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment to get.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, filter=None, top=None) -> web.Response:
    """deployments_list_by_resource_group

    Get all the deployments for a resource group.

    :param resource_group_name: The name of the resource group with the deployments to get. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;.
    :type filter: str
    :param top: The number of results to get. If null is passed, returns all deployments.
    :type top: int

    """
    return web.Response(status=200)


async def deployments_validate(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id, parameters) -> web.Response:
    """deployments_validate

    Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

    :param resource_group_name: The name of the resource group the template will be deployed to. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters to validate.
    :type parameters: dict | bytes

    """
    parameters = Deployment.from_dict(parameters)
    return web.Response(status=200)
