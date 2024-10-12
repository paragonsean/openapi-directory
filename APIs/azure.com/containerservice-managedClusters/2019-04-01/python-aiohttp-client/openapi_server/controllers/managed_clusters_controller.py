from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.credential_results import CredentialResults
from openapi_server.models.managed_cluster import ManagedCluster
from openapi_server.models.managed_cluster_aad_profile import ManagedClusterAADProfile
from openapi_server.models.managed_cluster_access_profile import ManagedClusterAccessProfile
from openapi_server.models.managed_cluster_list_result import ManagedClusterListResult
from openapi_server.models.managed_cluster_service_principal_profile import ManagedClusterServicePrincipalProfile
from openapi_server.models.managed_cluster_upgrade_profile import ManagedClusterUpgradeProfile
from openapi_server.models.tags_object import TagsObject
from openapi_server import util


async def managed_clusters_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, parameters) -> web.Response:
    """Creates or updates a managed cluster.

    Creates or updates a managed cluster with the specified configuration for agents and Kubernetes version.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str
    :param parameters: Parameters supplied to the Create or Update a Managed Cluster operation.
    :type parameters: dict | bytes

    """
    parameters = ManagedCluster.from_dict(parameters)
    return web.Response(status=200)


async def managed_clusters_delete(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Deletes a managed cluster.

    Deletes the managed cluster with a specified resource group and name.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def managed_clusters_get(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Gets a managed cluster.

    Gets the details of the managed cluster with a specified resource group and name.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def managed_clusters_get_access_profile(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, role_name) -> web.Response:
    """Gets an access profile of a managed cluster.

    Gets the accessProfile for the specified role name of the managed cluster with a specified resource group and name.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str
    :param role_name: The name of the role for managed cluster accessProfile resource.
    :type role_name: str

    """
    return web.Response(status=200)


async def managed_clusters_get_upgrade_profile(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Gets upgrade profile for a managed cluster.

    Gets the details of the upgrade profile for a managed cluster with a specified resource group and name.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def managed_clusters_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """Gets a list of managed clusters in the specified subscription.

    Gets a list of managed clusters in the specified subscription. The operation returns properties of each managed cluster.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def managed_clusters_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """Lists managed clusters in the specified subscription and resource group.

    Lists managed clusters in the specified subscription and resource group. The operation returns properties of each managed cluster.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def managed_clusters_list_cluster_admin_credentials(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Gets cluster admin credential of a managed cluster.

    Gets cluster admin credential of the managed cluster with a specified resource group and name.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def managed_clusters_list_cluster_user_credentials(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Gets cluster user credential of a managed cluster.

    Gets cluster user credential of the managed cluster with a specified resource group and name.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def managed_clusters_reset_aad_profile(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, parameters) -> web.Response:
    """Reset AAD Profile of a managed cluster.

    Update the AAD Profile for a managed cluster.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str
    :param parameters: Parameters supplied to the Reset AAD Profile operation for a Managed Cluster.
    :type parameters: dict | bytes

    """
    parameters = ManagedClusterAADProfile.from_dict(parameters)
    return web.Response(status=200)


async def managed_clusters_reset_service_principal_profile(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, parameters) -> web.Response:
    """Reset Service Principal Profile of a managed cluster.

    Update the service principal Profile for a managed cluster.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str
    :param parameters: Parameters supplied to the Reset Service Principal Profile operation for a Managed Cluster.
    :type parameters: dict | bytes

    """
    parameters = ManagedClusterServicePrincipalProfile.from_dict(parameters)
    return web.Response(status=200)


async def managed_clusters_update_tags(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, parameters) -> web.Response:
    """Updates tags on a managed cluster.

    Updates a managed cluster with the specified tags.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str
    :param parameters: Parameters supplied to the Update Managed Cluster Tags operation.
    :type parameters: dict | bytes

    """
    parameters = TagsObject.from_dict(parameters)
    return web.Response(status=200)
