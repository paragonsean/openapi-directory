from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.remediation import Remediation
from openapi_server.models.remediation_deployments_list_result import RemediationDeploymentsListResult
from openapi_server.models.remediation_list_result import RemediationListResult
from openapi_server import util


async def remediations_cancel_at_management_group(request: web.Request, management_groups_namespace, management_group_id, remediation_name, api_version) -> web.Response:
    """remediations_cancel_at_management_group

    Cancels a remediation at management group scope.

    :param management_groups_namespace: The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed.
    :type management_groups_namespace: str
    :param management_group_id: Management group ID.
    :type management_group_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def remediations_cancel_at_resource(request: web.Request, resource_id, remediation_name, api_version) -> web.Response:
    """remediations_cancel_at_resource

    Cancel a remediation at resource scope.

    :param resource_id: Resource ID.
    :type resource_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def remediations_cancel_at_resource_group(request: web.Request, subscription_id, resource_group_name, remediation_name, api_version) -> web.Response:
    """remediations_cancel_at_resource_group

    Cancels a remediation at resource group scope.

    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def remediations_cancel_at_subscription(request: web.Request, subscription_id, remediation_name, api_version) -> web.Response:
    """remediations_cancel_at_subscription

    Cancels a remediation at subscription scope.

    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def remediations_create_or_update_at_management_group(request: web.Request, management_groups_namespace, management_group_id, remediation_name, api_version, parameters) -> web.Response:
    """remediations_create_or_update_at_management_group

    Creates or updates a remediation at management group scope.

    :param management_groups_namespace: The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed.
    :type management_groups_namespace: str
    :param management_group_id: Management group ID.
    :type management_group_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The remediation parameters.
    :type parameters: dict | bytes

    """
    parameters = Remediation.from_dict(parameters)
    return web.Response(status=200)


async def remediations_create_or_update_at_resource(request: web.Request, resource_id, remediation_name, api_version, parameters) -> web.Response:
    """remediations_create_or_update_at_resource

    Creates or updates a remediation at resource scope.

    :param resource_id: Resource ID.
    :type resource_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The remediation parameters.
    :type parameters: dict | bytes

    """
    parameters = Remediation.from_dict(parameters)
    return web.Response(status=200)


async def remediations_create_or_update_at_resource_group(request: web.Request, subscription_id, resource_group_name, remediation_name, api_version, parameters) -> web.Response:
    """remediations_create_or_update_at_resource_group

    Creates or updates a remediation at resource group scope.

    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The remediation parameters.
    :type parameters: dict | bytes

    """
    parameters = Remediation.from_dict(parameters)
    return web.Response(status=200)


async def remediations_create_or_update_at_subscription(request: web.Request, subscription_id, remediation_name, api_version, parameters) -> web.Response:
    """remediations_create_or_update_at_subscription

    Creates or updates a remediation at subscription scope.

    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The remediation parameters.
    :type parameters: dict | bytes

    """
    parameters = Remediation.from_dict(parameters)
    return web.Response(status=200)


async def remediations_delete_at_management_group(request: web.Request, management_groups_namespace, management_group_id, remediation_name, api_version) -> web.Response:
    """remediations_delete_at_management_group

    Deletes an existing remediation at management group scope.

    :param management_groups_namespace: The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed.
    :type management_groups_namespace: str
    :param management_group_id: Management group ID.
    :type management_group_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def remediations_delete_at_resource(request: web.Request, resource_id, remediation_name, api_version) -> web.Response:
    """remediations_delete_at_resource

    Deletes an existing remediation at individual resource scope.

    :param resource_id: Resource ID.
    :type resource_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def remediations_delete_at_resource_group(request: web.Request, subscription_id, resource_group_name, remediation_name, api_version) -> web.Response:
    """remediations_delete_at_resource_group

    Deletes an existing remediation at resource group scope.

    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def remediations_delete_at_subscription(request: web.Request, subscription_id, remediation_name, api_version) -> web.Response:
    """remediations_delete_at_subscription

    Deletes an existing remediation at subscription scope.

    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def remediations_get_at_management_group(request: web.Request, management_groups_namespace, management_group_id, remediation_name, api_version) -> web.Response:
    """remediations_get_at_management_group

    Gets an existing remediation at management group scope.

    :param management_groups_namespace: The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed.
    :type management_groups_namespace: str
    :param management_group_id: Management group ID.
    :type management_group_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def remediations_get_at_resource(request: web.Request, resource_id, remediation_name, api_version) -> web.Response:
    """remediations_get_at_resource

    Gets an existing remediation at resource scope.

    :param resource_id: Resource ID.
    :type resource_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def remediations_get_at_resource_group(request: web.Request, subscription_id, resource_group_name, remediation_name, api_version) -> web.Response:
    """remediations_get_at_resource_group

    Gets an existing remediation at resource group scope.

    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def remediations_get_at_subscription(request: web.Request, subscription_id, remediation_name, api_version) -> web.Response:
    """remediations_get_at_subscription

    Gets an existing remediation at subscription scope.

    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def remediations_list_deployments_at_management_group(request: web.Request, management_groups_namespace, management_group_id, remediation_name, api_version, top=None) -> web.Response:
    """remediations_list_deployments_at_management_group

    Gets all deployments for a remediation at management group scope.

    :param management_groups_namespace: The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed.
    :type management_groups_namespace: str
    :param management_group_id: Management group ID.
    :type management_group_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int

    """
    return web.Response(status=200)


async def remediations_list_deployments_at_resource(request: web.Request, resource_id, remediation_name, api_version, top=None) -> web.Response:
    """remediations_list_deployments_at_resource

    Gets all deployments for a remediation at resource scope.

    :param resource_id: Resource ID.
    :type resource_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int

    """
    return web.Response(status=200)


async def remediations_list_deployments_at_resource_group(request: web.Request, subscription_id, resource_group_name, remediation_name, api_version, top=None) -> web.Response:
    """remediations_list_deployments_at_resource_group

    Gets all deployments for a remediation at resource group scope.

    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int

    """
    return web.Response(status=200)


async def remediations_list_deployments_at_subscription(request: web.Request, subscription_id, remediation_name, api_version, top=None) -> web.Response:
    """remediations_list_deployments_at_subscription

    Gets all deployments for a remediation at subscription scope.

    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param remediation_name: The name of the remediation.
    :type remediation_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int

    """
    return web.Response(status=200)


async def remediations_list_for_management_group(request: web.Request, management_groups_namespace, management_group_id, api_version, top=None, filter=None) -> web.Response:
    """remediations_list_for_management_group

    Gets all remediations for the management group.

    :param management_groups_namespace: The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed.
    :type management_groups_namespace: str
    :param management_group_id: Management group ID.
    :type management_group_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int
    :param filter: OData filter expression.
    :type filter: str

    """
    return web.Response(status=200)


async def remediations_list_for_resource(request: web.Request, resource_id, api_version, top=None, filter=None) -> web.Response:
    """remediations_list_for_resource

    Gets all remediations for a resource.

    :param resource_id: Resource ID.
    :type resource_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int
    :param filter: OData filter expression.
    :type filter: str

    """
    return web.Response(status=200)


async def remediations_list_for_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, top=None, filter=None) -> web.Response:
    """remediations_list_for_resource_group

    Gets all remediations for the subscription.

    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int
    :param filter: OData filter expression.
    :type filter: str

    """
    return web.Response(status=200)


async def remediations_list_for_subscription(request: web.Request, subscription_id, api_version, top=None, filter=None) -> web.Response:
    """remediations_list_for_subscription

    Gets all remediations for the subscription.

    :param subscription_id: Microsoft Azure subscription ID.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int
    :param filter: OData filter expression.
    :type filter: str

    """
    return web.Response(status=200)
