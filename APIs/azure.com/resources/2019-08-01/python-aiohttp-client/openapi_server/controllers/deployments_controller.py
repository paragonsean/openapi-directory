from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_export_result import DeploymentExportResult
from openapi_server.models.deployment_extended import DeploymentExtended
from openapi_server.models.deployment_list_result import DeploymentListResult
from openapi_server.models.deployment_validate_result import DeploymentValidateResult
from openapi_server.models.deployment_what_if import DeploymentWhatIf
from openapi_server.models.scoped_deployment import ScopedDeployment
from openapi_server.models.template_hash_result import TemplateHashResult
from openapi_server.models.what_if_operation_result import WhatIfOperationResult
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
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_cancel_at_management_group_scope(request: web.Request, group_id, deployment_name, api_version) -> web.Response:
    """Cancels a currently running template deployment.

    You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

    :param group_id: The management group ID.
    :type group_id: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_cancel_at_scope(request: web.Request, scope, deployment_name, api_version) -> web.Response:
    """Cancels a currently running template deployment.

    You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

    :param scope: The scope of a deployment.
    :type scope: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_cancel_at_subscription_scope(request: web.Request, deployment_name, api_version, subscription_id) -> web.Response:
    """Cancels a currently running template deployment.

    You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_cancel_at_tenant_scope(request: web.Request, deployment_name, api_version) -> web.Response:
    """Cancels a currently running template deployment.

    You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_check_existence(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_check_existence

    Checks whether the deployment exists.

    :param resource_group_name: The name of the resource group with the deployment to check. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_check_existence_at_management_group_scope(request: web.Request, group_id, deployment_name, api_version) -> web.Response:
    """deployments_check_existence_at_management_group_scope

    Checks whether the deployment exists.

    :param group_id: The management group ID.
    :type group_id: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_check_existence_at_scope(request: web.Request, scope, deployment_name, api_version) -> web.Response:
    """deployments_check_existence_at_scope

    Checks whether the deployment exists.

    :param scope: The scope of a deployment.
    :type scope: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_check_existence_at_subscription_scope(request: web.Request, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_check_existence_at_subscription_scope

    Checks whether the deployment exists.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_check_existence_at_tenant_scope(request: web.Request, deployment_name, api_version) -> web.Response:
    """deployments_check_existence_at_tenant_scope

    Checks whether the deployment exists.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

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


async def deployments_create_or_update_at_management_group_scope(request: web.Request, group_id, deployment_name, api_version, parameters) -> web.Response:
    """Deploys resources at management group scope.

    You can provide the template and parameters directly in the request or link to JSON files.

    :param group_id: The management group ID.
    :type group_id: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Additional parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = ScopedDeployment.from_dict(parameters)
    return web.Response(status=200)


async def deployments_create_or_update_at_scope(request: web.Request, scope, deployment_name, api_version, parameters) -> web.Response:
    """Deploys resources at a given scope.

    You can provide the template and parameters directly in the request or link to JSON files.

    :param scope: The scope of a deployment.
    :type scope: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Additional parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = Deployment.from_dict(parameters)
    return web.Response(status=200)


async def deployments_create_or_update_at_subscription_scope(request: web.Request, deployment_name, api_version, subscription_id, parameters) -> web.Response:
    """Deploys resources at subscription scope.

    You can provide the template and parameters directly in the request or link to JSON files.

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


async def deployments_create_or_update_at_tenant_scope(request: web.Request, deployment_name, api_version, parameters) -> web.Response:
    """Deploys resources at tenant scope.

    You can provide the template and parameters directly in the request or link to JSON files.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Additional parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = ScopedDeployment.from_dict(parameters)
    return web.Response(status=200)


async def deployments_delete(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """Deletes a deployment from the deployment history.

    A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. Deleting a template deployment does not affect the state of the resource group. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

    :param resource_group_name: The name of the resource group with the deployment to delete. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_delete_at_management_group_scope(request: web.Request, group_id, deployment_name, api_version) -> web.Response:
    """Deletes a deployment from the deployment history.

    A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

    :param group_id: The management group ID.
    :type group_id: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_delete_at_scope(request: web.Request, scope, deployment_name, api_version) -> web.Response:
    """Deletes a deployment from the deployment history.

    A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

    :param scope: The scope of a deployment.
    :type scope: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_delete_at_subscription_scope(request: web.Request, deployment_name, api_version, subscription_id) -> web.Response:
    """Deletes a deployment from the deployment history.

    A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_delete_at_tenant_scope(request: web.Request, deployment_name, api_version) -> web.Response:
    """Deletes a deployment from the deployment history.

    A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_export_template(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_export_template

    Exports the template used for specified deployment.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_export_template_at_management_group_scope(request: web.Request, group_id, deployment_name, api_version) -> web.Response:
    """deployments_export_template_at_management_group_scope

    Exports the template used for specified deployment.

    :param group_id: The management group ID.
    :type group_id: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_export_template_at_scope(request: web.Request, scope, deployment_name, api_version) -> web.Response:
    """deployments_export_template_at_scope

    Exports the template used for specified deployment.

    :param scope: The scope of a deployment.
    :type scope: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_export_template_at_subscription_scope(request: web.Request, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_export_template_at_subscription_scope

    Exports the template used for specified deployment.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_export_template_at_tenant_scope(request: web.Request, deployment_name, api_version) -> web.Response:
    """deployments_export_template_at_tenant_scope

    Exports the template used for specified deployment.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_get(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_get

    Gets a deployment.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_get_at_management_group_scope(request: web.Request, group_id, deployment_name, api_version) -> web.Response:
    """deployments_get_at_management_group_scope

    Gets a deployment.

    :param group_id: The management group ID.
    :type group_id: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_get_at_scope(request: web.Request, scope, deployment_name, api_version) -> web.Response:
    """deployments_get_at_scope

    Gets a deployment.

    :param scope: The scope of a deployment.
    :type scope: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_get_at_subscription_scope(request: web.Request, deployment_name, api_version, subscription_id) -> web.Response:
    """deployments_get_at_subscription_scope

    Gets a deployment.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def deployments_get_at_tenant_scope(request: web.Request, deployment_name, api_version) -> web.Response:
    """deployments_get_at_tenant_scope

    Gets a deployment.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployments_list_at_management_group_scope(request: web.Request, group_id, api_version, filter=None, top=None) -> web.Response:
    """deployments_list_at_management_group_scope

    Get all the deployments for a management group.

    :param group_id: The management group ID.
    :type group_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param filter: The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;.
    :type filter: str
    :param top: The number of results to get. If null is passed, returns all deployments.
    :type top: int

    """
    return web.Response(status=200)


async def deployments_list_at_scope(request: web.Request, scope, api_version, filter=None, top=None) -> web.Response:
    """deployments_list_at_scope

    Get all the deployments at the given scope.

    :param scope: The scope of a deployment.
    :type scope: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param filter: The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;.
    :type filter: str
    :param top: The number of results to get. If null is passed, returns all deployments.
    :type top: int

    """
    return web.Response(status=200)


async def deployments_list_at_subscription_scope(request: web.Request, api_version, subscription_id, filter=None, top=None) -> web.Response:
    """deployments_list_at_subscription_scope

    Get all the deployments for a subscription.

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


async def deployments_list_at_tenant_scope(request: web.Request, api_version, filter=None, top=None) -> web.Response:
    """deployments_list_at_tenant_scope

    Get all the deployments at the tenant scope.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param filter: The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;.
    :type filter: str
    :param top: The number of results to get. If null is passed, returns all deployments.
    :type top: int

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


async def deployments_validate_at_management_group_scope(request: web.Request, group_id, deployment_name, api_version, parameters) -> web.Response:
    """deployments_validate_at_management_group_scope

    Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

    :param group_id: The management group ID.
    :type group_id: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Parameters to validate.
    :type parameters: dict | bytes

    """
    parameters = ScopedDeployment.from_dict(parameters)
    return web.Response(status=200)


async def deployments_validate_at_scope(request: web.Request, scope, deployment_name, api_version, parameters) -> web.Response:
    """deployments_validate_at_scope

    Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

    :param scope: The scope of a deployment.
    :type scope: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Parameters to validate.
    :type parameters: dict | bytes

    """
    parameters = Deployment.from_dict(parameters)
    return web.Response(status=200)


async def deployments_validate_at_subscription_scope(request: web.Request, deployment_name, api_version, subscription_id, parameters) -> web.Response:
    """deployments_validate_at_subscription_scope

    Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

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


async def deployments_validate_at_tenant_scope(request: web.Request, deployment_name, api_version, parameters) -> web.Response:
    """deployments_validate_at_tenant_scope

    Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Parameters to validate.
    :type parameters: dict | bytes

    """
    parameters = ScopedDeployment.from_dict(parameters)
    return web.Response(status=200)


async def deployments_what_if(request: web.Request, resource_group_name, deployment_name, api_version, subscription_id, parameters) -> web.Response:
    """deployments_what_if

    Returns changes that will be made by the deployment if executed at the scope of the resource group.

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
    parameters = DeploymentWhatIf.from_dict(parameters)
    return web.Response(status=200)


async def deployments_what_if_at_subscription_scope(request: web.Request, deployment_name, api_version, subscription_id, parameters) -> web.Response:
    """deployments_what_if_at_subscription_scope

    Returns changes that will be made by the deployment if executed at the scope of the subscription.

    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters to What If.
    :type parameters: dict | bytes

    """
    parameters = DeploymentWhatIf.from_dict(parameters)
    return web.Response(status=200)
