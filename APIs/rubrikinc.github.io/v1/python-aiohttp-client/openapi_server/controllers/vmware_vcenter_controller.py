from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.hot_add_bandwidth_info import HotAddBandwidthInfo
from openapi_server.models.hot_add_network_config_with_id import HotAddNetworkConfigWithId
from openapi_server.models.hot_add_network_config_with_name import HotAddNetworkConfigWithName
from openapi_server.models.hot_add_proxies_needed_info import HotAddProxiesNeededInfo
from openapi_server.models.hot_add_proxy_vm_info_list_response import HotAddProxyVmInfoListResponse
from openapi_server.models.network_info_list_response import NetworkInfoListResponse
from openapi_server.models.vcenter_config import VcenterConfig
from openapi_server.models.vcenter_detail import VcenterDetail
from openapi_server.models.vcenter_patch import VcenterPatch
from openapi_server.models.vcenter_summary import VcenterSummary
from openapi_server.models.vcenter_summary_list_response import VcenterSummaryListResponse
from openapi_server import util


async def create_refresh(request: web.Request, id) -> web.Response:
    """Refresh vCenter Server metadata

    Create a job to refresh the metadata for the specified vCenter Server.

    :param id: ID of the vCenter Server.
    :type id: str

    """
    return web.Response(status=200)


async def create_refresh_vm_v1(request: web.Request, id, body) -> web.Response:
    """Refresh single virtual machine metadata in a vcenter

    Refresh the metadata for a single virtual machine controlled by vCenter.

    :param id: The ID of the vCenter server that controls the management of the virtual machine whose metadata will be refreshed.
    :type id: str
    :param body: The vCenter managed object ID (MOID) of the virtual machine whose metadata will be refreshed.
    :type body: str

    """
    return web.Response(status=200)


async def create_vcenter(request: web.Request, body) -> web.Response:
    """Add vCenter Server

    (DEPRECATED) Create a vCenter Server object by providing the address and account credentials of the vCenter Server. Initiates an asynchronous job to establish a connection with the vCenter Server and retrieve all metadata. Use GET /vcenter/{id}/status to check status. The recommended endpoint is /v2/vmware/vcenter. This endpoint will remain available in future releases despite deprecation.

    :param body: IP address and account credentials of the vCenter Server server, and ID of the managing Rubrik cluster.
    :type body: dict | bytes

    """
    body = VcenterConfig.from_dict(body)
    return web.Response(status=200)


async def delete_vcenter(request: web.Request, id) -> web.Response:
    """Remove vCenter Server

    Initiates an asynchronous job to remove a vCenter Server object. The vCenter Server cannot have VMs mounted through the Rubrik cluster.

    :param id: ID of the vCenter Server. to remove.
    :type id: str

    """
    return web.Response(status=200)


async def get_hot_add_bandwidth(request: web.Request, id) -> web.Response:
    """Get the ingest and export bandwidth limits for HotAdd with the vCenter

    Get the ingest and export bandwidth limits in Mbps when using HotAdd with the vCenter. These limits are shared across all HotAdd proxies for the Center.

    :param id: The ID of the vCenter server from which to derive the number of proxies needed.
    :type id: str

    """
    return web.Response(status=200)


async def get_hot_add_network(request: web.Request, id) -> web.Response:
    """Retrieve the user-configured network for HotAdd operations

    Retrieve the user-configured network for HotAdd backup and recovery operations on VMware on AWS.

    :param id: ID of the vCenter server for which the Rubrik cluster is retrieving the configured HotAdd network information.
    :type id: str

    """
    return web.Response(status=200)


async def get_networks(request: web.Request, id) -> web.Response:
    """Get the user-configured networks in the vCenter

    Get the names and IDs of the user configured networks in the vCenter. This information enables users to choose a desired network for backups to go through for VMware Cloud on AWS setups.

    :param id: The ID of the vCenter server for which to retrieve user-configured networks.
    :type id: str

    """
    return web.Response(status=200)


async def get_num_proxies_needed(request: web.Request, id) -> web.Response:
    """Get the number of HotAdd proxies needed for the vCenter

    Get the number of HotAdd proxies that need to be deployed to the vCenter to support the maximum number of ingest jobs.

    :param id: The ID of the vCenter server for which to get the number of proxies needed.
    :type id: str

    """
    return web.Response(status=200)


async def get_vcenter(request: web.Request, id) -> web.Response:
    """Get the details of a vCenter Server

    Retrieve detailed information for a vCenter Server object.

    :param id: ID of the vCenter Server.
    :type id: str

    """
    return web.Response(status=200)


async def get_vcenter_async_request_status(request: web.Request, id) -> web.Response:
    """Get vCenter Server async request

    Get details about a vcenter related async request.

    :param id: ID of the request.
    :type id: str

    """
    return web.Response(status=200)


async def patch_vcenter(request: web.Request, id, body) -> web.Response:
    """Update the SLA Domain for a vCenter Server

    Update the SLA Domain that is configured for a vCenter Server.

    :param id: ID of the vCenter Server.
    :type id: str
    :param body: Object containing updated vCenter Server information.
    :type body: dict | bytes

    """
    body = VcenterPatch.from_dict(body)
    return web.Response(status=200)


async def query_hot_add_proxy_vm(request: web.Request, name=None, sort_by=None, sort_order=None) -> web.Response:
    """Get a list of HotAdd proxy virtual machines

    Retrieve summary information for all HotAdd proxy virtual machines.

    :param name: Limit the list information to HotAdd proxy virtual machines that match the specified HotAdd proxy virtual machine &#39;name&#39; value.
    :type name: str
    :param sort_by: Attribute to use to sort the HotAdd proxy virtual machines summary information. Optionally use **_sort_order_** to specify whether to sort in ascending or descending order.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def query_vcenter(request: web.Request, primary_cluster_id=None, snappable_status=None, ignore_connection_status=None) -> web.Response:
    """Get list of vCenters

    Retrieve information for each managed vCenter, including: ID, managed ID, address, username, SLA ID, and primary cluster ID.

    :param primary_cluster_id: Limits the information to the Rubrik cluster specified by the value of primary_cluster_id. Use &#39;local&#39; for the Rubrik cluster that is hosting the current REST API session.
    :type primary_cluster_id: str
    :param snappable_status: Determines whether to fetch vCenters with additional privilege checks.
    :type snappable_status: str
    :param ignore_connection_status: Don&#39;t ping vCenters for connection status. The connection_status field in the response is unusable.
    :type ignore_connection_status: bool

    """
    return web.Response(status=200)


async def set_hot_add_bandwidth(request: web.Request, id, body) -> web.Response:
    """Set the ingest and export bandwidth limits for HotAdd with the vCenter

    Set the ingest and export bandwidth limits in Mbps when using HotAdd with the vCenter. These limits are shared across all HotAdd proxies for the Center.

    :param id: ID of the vCenter server upon which the Rubrik cluster is setting the HotAdd bandwidth limits.
    :type id: str
    :param body: The ingest and export bandwidth limits for the vCenter.
    :type body: dict | bytes

    """
    body = HotAddBandwidthInfo.from_dict(body)
    return web.Response(status=200)


async def set_hot_add_network(request: web.Request, id, body) -> web.Response:
    """Set the user-configured network for HotAdd backup and recovery

    Set the user-configured network for HotAdd backup and recovery operations on VMware on AWS.

    :param id: ID of the vCenter server for which the Rubrik cluster is setting the HotAdd network information.
    :type id: str
    :param body: The information about a static IP address and user-configured vCenter network selected for HotAdd backup and recovery.
    :type body: dict | bytes

    """
    body = HotAddNetworkConfigWithId.from_dict(body)
    return web.Response(status=200)


async def update_vcenter(request: web.Request, id, body) -> web.Response:
    """Update vCenter Server

    Update the address, username and password of the specified vCenter Server object.

    :param id: ID of the vCenter Server.
    :type id: str
    :param body: Object containing updated vCenter Server information.
    :type body: dict | bytes

    """
    body = VcenterConfig.from_dict(body)
    return web.Response(status=200)
