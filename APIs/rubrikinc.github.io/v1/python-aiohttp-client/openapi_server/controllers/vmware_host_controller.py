from typing import List, Dict
from aiohttp import web

from openapi_server.models.vmware_host_datastore_detail import VmwareHostDatastoreDetail
from openapi_server.models.vmware_host_detail import VmwareHostDetail
from openapi_server.models.vmware_host_summary_list_response import VmwareHostSummaryListResponse
from openapi_server.models.vmware_host_update import VmwareHostUpdate
from openapi_server import util


async def get_vmware_host(request: web.Request, id) -> web.Response:
    """Get details of a ESXi hypervisor

    Get details of a ESXi hypervisor.

    :param id: ID of the VMWare host.
    :type id: str

    """
    return web.Response(status=200)


async def get_vmware_host_datastore(request: web.Request, id) -> web.Response:
    """Get details of datastores in a ESXi hypervisor

    Get details of datastores in a ESXi hypervisor.

    :param id: ID of the VMWare host.
    :type id: str

    """
    return web.Response(status=200)


async def query_vmware_host(request: web.Request, primary_cluster_id=None, compute_cluster_id=None, snappable_status=None) -> web.Response:
    """Get summary of all the ESXi hypervisor

    Get summary of all the ESXi hypervisor.

    :param primary_cluster_id: ID of the Primary cluster.
    :type primary_cluster_id: str
    :param compute_cluster_id: Filter by ID of Compute Cluster.
    :type compute_cluster_id: str
    :param snappable_status: Requests additional data about VMware Hosts based on the specified query value.
    :type snappable_status: str

    """
    return web.Response(status=200)


async def update_vmware_host(request: web.Request, id, body) -> web.Response:
    """Update the SLA Domain for an ESXi hypervisor

    Update the SLA Domain that is configured for an ESXi hypervisor.

    :param id: ID of the ESXi hypervisor.
    :type id: str
    :param body: Object with changes for the ESXi hypervisor information.
    :type body: dict | bytes

    """
    body = VmwareHostUpdate.from_dict(body)
    return web.Response(status=200)
