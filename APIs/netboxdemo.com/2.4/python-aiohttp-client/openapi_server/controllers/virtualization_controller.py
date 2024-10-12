from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_group import ClusterGroup
from openapi_server.models.cluster_type import ClusterType
from openapi_server.models.dcim_interfaces_list200_response import DcimInterfacesList200Response
from openapi_server.models.interface import Interface
from openapi_server.models.virtual_machine import VirtualMachine
from openapi_server.models.virtual_machine_with_config_context import VirtualMachineWithConfigContext
from openapi_server.models.virtualization_cluster_groups_list200_response import VirtualizationClusterGroupsList200Response
from openapi_server.models.virtualization_cluster_types_list200_response import VirtualizationClusterTypesList200Response
from openapi_server.models.virtualization_clusters_list200_response import VirtualizationClustersList200Response
from openapi_server.models.virtualization_virtual_machines_list200_response import VirtualizationVirtualMachinesList200Response
from openapi_server.models.writable_cluster import WritableCluster
from openapi_server.models.writable_interface import WritableInterface
from openapi_server.models.writable_virtual_machine import WritableVirtualMachine
from openapi_server import util


async def virtualization_choices_list(request: web.Request, ) -> web.Response:
    """virtualization_choices_list

    


    """
    return web.Response(status=200)


async def virtualization_choices_read(request: web.Request, id) -> web.Response:
    """virtualization_choices_read

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


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


async def virtualization_cluster_groups_list(request: web.Request, name=None, slug=None, limit=None, offset=None) -> web.Response:
    """virtualization_cluster_groups_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
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


async def virtualization_cluster_types_list(request: web.Request, name=None, slug=None, limit=None, offset=None) -> web.Response:
    """virtualization_cluster_types_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
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


async def virtualization_clusters_list(request: web.Request, name=None, id__in=None, q=None, group_id=None, group=None, type_id=None, type=None, site_id=None, site=None, tag=None, limit=None, offset=None) -> web.Response:
    """virtualization_clusters_list

    

    :param name: 
    :type name: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param q: 
    :type q: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
    :param type_id: 
    :type type_id: str
    :param type: 
    :type type: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param tag: 
    :type tag: str
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
    body = WritableInterface.from_dict(body)
    return web.Response(status=200)


async def virtualization_interfaces_delete(request: web.Request, id) -> web.Response:
    """virtualization_interfaces_delete

    

    :param id: A unique integer value identifying this interface.
    :type id: int

    """
    return web.Response(status=200)


async def virtualization_interfaces_list(request: web.Request, name=None, enabled=None, mtu=None, virtual_machine_id=None, virtual_machine=None, mac_address=None, limit=None, offset=None) -> web.Response:
    """virtualization_interfaces_list

    

    :param name: 
    :type name: str
    :param enabled: 
    :type enabled: str
    :param mtu: 
    :type mtu: 
    :param virtual_machine_id: 
    :type virtual_machine_id: str
    :param virtual_machine: 
    :type virtual_machine: str
    :param mac_address: 
    :type mac_address: str
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
    body = WritableInterface.from_dict(body)
    return web.Response(status=200)


async def virtualization_interfaces_read(request: web.Request, id) -> web.Response:
    """virtualization_interfaces_read

    

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
    body = WritableInterface.from_dict(body)
    return web.Response(status=200)


async def virtualization_virtual_machines_create(request: web.Request, body) -> web.Response:
    """virtualization_virtual_machines_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVirtualMachine.from_dict(body)
    return web.Response(status=200)


async def virtualization_virtual_machines_delete(request: web.Request, id) -> web.Response:
    """virtualization_virtual_machines_delete

    

    :param id: A unique integer value identifying this virtual machine.
    :type id: int

    """
    return web.Response(status=200)


async def virtualization_virtual_machines_list(request: web.Request, name=None, cluster=None, id__in=None, q=None, status=None, cluster_group_id=None, cluster_group=None, cluster_type_id=None, cluster_type=None, cluster_id=None, region_id=None, region=None, site_id=None, site=None, role_id=None, role=None, tenant_id=None, tenant=None, platform_id=None, platform=None, tag=None, limit=None, offset=None) -> web.Response:
    """virtualization_virtual_machines_list

    

    :param name: 
    :type name: str
    :param cluster: 
    :type cluster: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
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
    :type region_id: 
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
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param platform_id: 
    :type platform_id: str
    :param platform: 
    :type platform: str
    :param tag: 
    :type tag: str
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
    body = WritableVirtualMachine.from_dict(body)
    return web.Response(status=200)


async def virtualization_virtual_machines_read(request: web.Request, id) -> web.Response:
    """virtualization_virtual_machines_read

    

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
    body = WritableVirtualMachine.from_dict(body)
    return web.Response(status=200)
