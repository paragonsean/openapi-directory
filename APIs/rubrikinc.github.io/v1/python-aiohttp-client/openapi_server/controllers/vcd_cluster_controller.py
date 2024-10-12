from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.vcd_cluster_config import VcdClusterConfig
from openapi_server.models.vcd_cluster_detail import VcdClusterDetail
from openapi_server.models.vcd_cluster_patch import VcdClusterPatch
from openapi_server.models.vcd_cluster_summary_list_response import VcdClusterSummaryListResponse
from openapi_server.models.vimserver_summary_list_response import VimserverSummaryListResponse
from openapi_server import util


async def create_vcd_cluster_v1(request: web.Request, body) -> web.Response:
    """Add a vCD Cluster

    Create a vCD Cluster object by providing the address of the vCD Cluster and the credentials for an account on the vCD Cluster that has administrator privileges. This request initiates an asynchronous job to connect with the vCD Cluster and retrieve the required metadata.

    :param body: IP address and account credentials of the vCD Cluster, and ID of the managing Rubrik cluster.
    :type body: dict | bytes

    """
    body = VcdClusterConfig.from_dict(body)
    return web.Response(status=200)


async def delete_vcd_cluster_v1(request: web.Request, id) -> web.Response:
    """Remove vCD Cluster

    Start an asynchronous job to remove a vCD Cluster object.

    :param id: ID assigned to a vCD Cluster object.
    :type id: str

    """
    return web.Response(status=200)


async def get_vcd_cluster_async_request_status_v1(request: web.Request, id) -> web.Response:
    """Get vCD Cluster job status

    Retrieve the details of a specified asynchronous job for a vCD Cluster.

    :param id: ID assigned to an asynchronous job.
    :type id: str

    """
    return web.Response(status=200)


async def get_vcd_cluster_v1(request: web.Request, id) -> web.Response:
    """Get vCD Cluster details

    Retrieve detailed information for a vCD Cluster object.

    :param id: ID assigned to a vCD Cluster object.
    :type id: str

    """
    return web.Response(status=200)


async def query_vcd_cluster_v1(request: web.Request, name=None, status=None, sort_by=None, sort_order=None) -> web.Response:
    """Get summary for all vCD Clusters

    Retrieve summary information for all vCD cluster objects.

    :param name: Search for a vCD Cluster object by name.
    :type name: str
    :param status: Filter the results using the status value of the vCD Cluster objects.
    :type status: str
    :param sort_by: Attribute to sort the results on.
    :type sort_by: str
    :param sort_order: Order for sorting the results, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def query_vcd_vim_server_v1(request: web.Request, id, sort_by=None, sort_order=None) -> web.Response:
    """Get VimServers of a vCD Cluster

    Retrieves the VimServer representation of the vCenter Servers that are attached to a specified vCD Cluster object.

    :param id: ID assigned to a vCD Cluster object.
    :type id: str
    :param sort_by: Attribute to sort the results on.
    :type sort_by: str
    :param sort_order: Order for sorting the results, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def refresh_vcd_cluster_v1(request: web.Request, id) -> web.Response:
    """Refresh a vCD Cluster

    Start an asynchronous job to refresh the metadata for a specified vCD Cluster object.

    :param id: ID assigned to a vCD Cluster object.
    :type id: str

    """
    return web.Response(status=200)


async def update_vcd_cluster_v1(request: web.Request, id, body) -> web.Response:
    """Change vCD Cluster object

    Modify the hostname and credentials of a specified vCD Cluster object.

    :param id: ID assigned to a vCD Cluster object.
    :type id: str
    :param body: Updated hostname and credentials for a specified vCD Cluster object.
    :type body: dict | bytes

    """
    body = VcdClusterPatch.from_dict(body)
    return web.Response(status=200)
