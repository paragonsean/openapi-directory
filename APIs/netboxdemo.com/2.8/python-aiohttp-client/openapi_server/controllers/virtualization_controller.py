from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_group import ClusterGroup
from openapi_server.models.cluster_type import ClusterType
from openapi_server.models.virtual_machine_interface import VirtualMachineInterface
from openapi_server.models.virtual_machine_with_config_context import VirtualMachineWithConfigContext
from openapi_server.models.virtualization_cluster_groups_list200_response import VirtualizationClusterGroupsList200Response
from openapi_server.models.virtualization_cluster_types_list200_response import VirtualizationClusterTypesList200Response
from openapi_server.models.virtualization_clusters_list200_response import VirtualizationClustersList200Response
from openapi_server.models.virtualization_interfaces_list200_response import VirtualizationInterfacesList200Response
from openapi_server.models.virtualization_virtual_machines_list200_response import VirtualizationVirtualMachinesList200Response
from openapi_server.models.writable_cluster import WritableCluster
from openapi_server.models.writable_virtual_machine_interface import WritableVirtualMachineInterface
from openapi_server.models.writable_virtual_machine_with_config_context import WritableVirtualMachineWithConfigContext
from openapi_server import util


async def virtualization_cluster_groups_create(request: web.Request, body) -> web.Response:
    """virtualization_cluster_groups_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = ClusterGroup.from_dict(body)
    return web.Response(status=200)


async def virtualization_cluster_groups_delete(request: web.Request, id) -> web.Response:
    """virtualization_cluster_groups_delete

    

    :param id: A unique integer value identifying this cluster group.
    :type id: int

    """
    return web.Response(status=200)


async def virtualization_cluster_groups_list(request: web.Request, id=None, name=None, slug=None, description=None, q=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, limit=None, offset=None) -> web.Response:
    """virtualization_cluster_groups_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def virtualization_cluster_groups_partial_update(request: web.Request, id, body) -> web.Response:
    """virtualization_cluster_groups_partial_update

    

    :param id: A unique integer value identifying this cluster group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ClusterGroup.from_dict(body)
    return web.Response(status=200)


async def virtualization_cluster_groups_read(request: web.Request, id) -> web.Response:
    """virtualization_cluster_groups_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this cluster group.
    :type id: int

    """
    return web.Response(status=200)


async def virtualization_cluster_groups_update(request: web.Request, id, body) -> web.Response:
    """virtualization_cluster_groups_update

    

    :param id: A unique integer value identifying this cluster group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ClusterGroup.from_dict(body)
    return web.Response(status=200)


async def virtualization_cluster_types_create(request: web.Request, body) -> web.Response:
    """virtualization_cluster_types_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = ClusterType.from_dict(body)
    return web.Response(status=200)


async def virtualization_cluster_types_delete(request: web.Request, id) -> web.Response:
    """virtualization_cluster_types_delete

    

    :param id: A unique integer value identifying this cluster type.
    :type id: int

    """
    return web.Response(status=200)


async def virtualization_cluster_types_list(request: web.Request, id=None, name=None, slug=None, description=None, q=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, limit=None, offset=None) -> web.Response:
    """virtualization_cluster_types_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def virtualization_cluster_types_partial_update(request: web.Request, id, body) -> web.Response:
    """virtualization_cluster_types_partial_update

    

    :param id: A unique integer value identifying this cluster type.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ClusterType.from_dict(body)
    return web.Response(status=200)


async def virtualization_cluster_types_read(request: web.Request, id) -> web.Response:
    """virtualization_cluster_types_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this cluster type.
    :type id: int

    """
    return web.Response(status=200)


async def virtualization_cluster_types_update(request: web.Request, id, body) -> web.Response:
    """virtualization_cluster_types_update

    

    :param id: A unique integer value identifying this cluster type.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ClusterType.from_dict(body)
    return web.Response(status=200)


async def virtualization_clusters_create(request: web.Request, body) -> web.Response:
    """virtualization_clusters_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableCluster.from_dict(body)
    return web.Response(status=200)


async def virtualization_clusters_delete(request: web.Request, id) -> web.Response:
    """virtualization_clusters_delete

    

    :param id: A unique integer value identifying this cluster.
    :type id: int

    """
    return web.Response(status=200)


async def virtualization_clusters_list(request: web.Request, id=None, name=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, region_id=None, region=None, site_id=None, site=None, group_id=None, group=None, type_id=None, type=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, group_id__n=None, group__n=None, type_id__n=None, type__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """virtualization_clusters_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
    :param type_id: 
    :type type_id: str
    :param type: 
    :type type: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param group_id__n: 
    :type group_id__n: str
    :param group__n: 
    :type group__n: str
    :param type_id__n: 
    :type type_id__n: str
    :param type__n: 
    :type type__n: str
    :param tag__n: 
    :type tag__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def virtualization_clusters_partial_update(request: web.Request, id, body) -> web.Response:
    """virtualization_clusters_partial_update

    

    :param id: A unique integer value identifying this cluster.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableCluster.from_dict(body)
    return web.Response(status=200)


async def virtualization_clusters_read(request: web.Request, id) -> web.Response:
    """virtualization_clusters_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this cluster.
    :type id: int

    """
    return web.Response(status=200)


async def virtualization_clusters_update(request: web.Request, id, body) -> web.Response:
    """virtualization_clusters_update

    

    :param id: A unique integer value identifying this cluster.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableCluster.from_dict(body)
    return web.Response(status=200)


async def virtualization_interfaces_create(request: web.Request, body) -> web.Response:
    """virtualization_interfaces_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualMachineInterface.from_dict(body)
    return web.Response(status=200)


async def virtualization_interfaces_delete(request: web.Request, id) -> web.Response:
    """virtualization_interfaces_delete

    

    :param id: A unique integer value identifying this interface.
    :type id: int

    """
    return web.Response(status=200)


async def virtualization_interfaces_list(request: web.Request, id=None, name=None, enabled=None, mtu=None, q=None, virtual_machine_id=None, virtual_machine=None, mac_address=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, mtu__n=None, mtu__lte=None, mtu__lt=None, mtu__gte=None, mtu__gt=None, virtual_machine_id__n=None, virtual_machine__n=None, mac_address__n=None, mac_address__ic=None, mac_address__nic=None, mac_address__iew=None, mac_address__niew=None, mac_address__isw=None, mac_address__nisw=None, mac_address__ie=None, mac_address__nie=None, limit=None, offset=None) -> web.Response:
    """virtualization_interfaces_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param enabled: 
    :type enabled: str
    :param mtu: 
    :type mtu: str
    :param q: 
    :type q: str
    :param virtual_machine_id: 
    :type virtual_machine_id: str
    :param virtual_machine: 
    :type virtual_machine: str
    :param mac_address: 
    :type mac_address: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param mtu__n: 
    :type mtu__n: str
    :param mtu__lte: 
    :type mtu__lte: str
    :param mtu__lt: 
    :type mtu__lt: str
    :param mtu__gte: 
    :type mtu__gte: str
    :param mtu__gt: 
    :type mtu__gt: str
    :param virtual_machine_id__n: 
    :type virtual_machine_id__n: str
    :param virtual_machine__n: 
    :type virtual_machine__n: str
    :param mac_address__n: 
    :type mac_address__n: str
    :param mac_address__ic: 
    :type mac_address__ic: str
    :param mac_address__nic: 
    :type mac_address__nic: str
    :param mac_address__iew: 
    :type mac_address__iew: str
    :param mac_address__niew: 
    :type mac_address__niew: str
    :param mac_address__isw: 
    :type mac_address__isw: str
    :param mac_address__nisw: 
    :type mac_address__nisw: str
    :param mac_address__ie: 
    :type mac_address__ie: str
    :param mac_address__nie: 
    :type mac_address__nie: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def virtualization_interfaces_partial_update(request: web.Request, id, body) -> web.Response:
    """virtualization_interfaces_partial_update

    

    :param id: A unique integer value identifying this interface.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualMachineInterface.from_dict(body)
    return web.Response(status=200)


async def virtualization_interfaces_read(request: web.Request, id) -> web.Response:
    """virtualization_interfaces_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this interface.
    :type id: int

    """
    return web.Response(status=200)


async def virtualization_interfaces_update(request: web.Request, id, body) -> web.Response:
    """virtualization_interfaces_update

    

    :param id: A unique integer value identifying this interface.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualMachineInterface.from_dict(body)
    return web.Response(status=200)


async def virtualization_virtual_machines_create(request: web.Request, body) -> web.Response:
    """virtualization_virtual_machines_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualMachineWithConfigContext.from_dict(body)
    return web.Response(status=200)


async def virtualization_virtual_machines_delete(request: web.Request, id) -> web.Response:
    """virtualization_virtual_machines_delete

    

    :param id: A unique integer value identifying this virtual machine.
    :type id: int

    """
    return web.Response(status=200)


async def virtualization_virtual_machines_list(request: web.Request, id=None, name=None, cluster=None, vcpus=None, memory=None, disk=None, local_context_data=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, status=None, cluster_group_id=None, cluster_group=None, cluster_type_id=None, cluster_type=None, cluster_id=None, region_id=None, region=None, site_id=None, site=None, role_id=None, role=None, platform_id=None, platform=None, mac_address=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, cluster__n=None, vcpus__n=None, vcpus__lte=None, vcpus__lt=None, vcpus__gte=None, vcpus__gt=None, memory__n=None, memory__lte=None, memory__lt=None, memory__gte=None, memory__gt=None, disk__n=None, disk__lte=None, disk__lt=None, disk__gte=None, disk__gt=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, status__n=None, cluster_group_id__n=None, cluster_group__n=None, cluster_type_id__n=None, cluster_type__n=None, cluster_id__n=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, role_id__n=None, role__n=None, platform_id__n=None, platform__n=None, mac_address__n=None, mac_address__ic=None, mac_address__nic=None, mac_address__iew=None, mac_address__niew=None, mac_address__isw=None, mac_address__nisw=None, mac_address__ie=None, mac_address__nie=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """virtualization_virtual_machines_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param cluster: 
    :type cluster: str
    :param vcpus: 
    :type vcpus: str
    :param memory: 
    :type memory: str
    :param disk: 
    :type disk: str
    :param local_context_data: 
    :type local_context_data: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param status: 
    :type status: str
    :param cluster_group_id: 
    :type cluster_group_id: str
    :param cluster_group: 
    :type cluster_group: str
    :param cluster_type_id: 
    :type cluster_type_id: str
    :param cluster_type: 
    :type cluster_type: str
    :param cluster_id: 
    :type cluster_id: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param platform_id: 
    :type platform_id: str
    :param platform: 
    :type platform: str
    :param mac_address: 
    :type mac_address: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param cluster__n: 
    :type cluster__n: str
    :param vcpus__n: 
    :type vcpus__n: str
    :param vcpus__lte: 
    :type vcpus__lte: str
    :param vcpus__lt: 
    :type vcpus__lt: str
    :param vcpus__gte: 
    :type vcpus__gte: str
    :param vcpus__gt: 
    :type vcpus__gt: str
    :param memory__n: 
    :type memory__n: str
    :param memory__lte: 
    :type memory__lte: str
    :param memory__lt: 
    :type memory__lt: str
    :param memory__gte: 
    :type memory__gte: str
    :param memory__gt: 
    :type memory__gt: str
    :param disk__n: 
    :type disk__n: str
    :param disk__lte: 
    :type disk__lte: str
    :param disk__lt: 
    :type disk__lt: str
    :param disk__gte: 
    :type disk__gte: str
    :param disk__gt: 
    :type disk__gt: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param status__n: 
    :type status__n: str
    :param cluster_group_id__n: 
    :type cluster_group_id__n: str
    :param cluster_group__n: 
    :type cluster_group__n: str
    :param cluster_type_id__n: 
    :type cluster_type_id__n: str
    :param cluster_type__n: 
    :type cluster_type__n: str
    :param cluster_id__n: 
    :type cluster_id__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param platform_id__n: 
    :type platform_id__n: str
    :param platform__n: 
    :type platform__n: str
    :param mac_address__n: 
    :type mac_address__n: str
    :param mac_address__ic: 
    :type mac_address__ic: str
    :param mac_address__nic: 
    :type mac_address__nic: str
    :param mac_address__iew: 
    :type mac_address__iew: str
    :param mac_address__niew: 
    :type mac_address__niew: str
    :param mac_address__isw: 
    :type mac_address__isw: str
    :param mac_address__nisw: 
    :type mac_address__nisw: str
    :param mac_address__ie: 
    :type mac_address__ie: str
    :param mac_address__nie: 
    :type mac_address__nie: str
    :param tag__n: 
    :type tag__n: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def virtualization_virtual_machines_partial_update(request: web.Request, id, body) -> web.Response:
    """virtualization_virtual_machines_partial_update

    

    :param id: A unique integer value identifying this virtual machine.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualMachineWithConfigContext.from_dict(body)
    return web.Response(status=200)


async def virtualization_virtual_machines_read(request: web.Request, id) -> web.Response:
    """virtualization_virtual_machines_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this virtual machine.
    :type id: int

    """
    return web.Response(status=200)


async def virtualization_virtual_machines_update(request: web.Request, id, body) -> web.Response:
    """virtualization_virtual_machines_update

    

    :param id: A unique integer value identifying this virtual machine.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualMachineWithConfigContext.from_dict(body)
    return web.Response(status=200)
