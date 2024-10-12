from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.compute_cluster_detail import ComputeClusterDetail
from openapi_server.models.compute_cluster_summary_list_response import ComputeClusterSummaryListResponse
from openapi_server.models.compute_cluster_update import ComputeClusterUpdate
from openapi_server.models.fully_qualified_domain_name_info import FullyQualifiedDomainNameInfo
from openapi_server.models.io_filter_summary_list_response import IoFilterSummaryListResponse
from openapi_server import util


async def get_async_request_status_for_compute_cluster(request: web.Request, id) -> web.Response:
    """Get asynchronous request details for VMware cluster

    Get the details of an asynchronous request that involves a VMware compute cluster.

    :param id: ID of an asynchronous request.
    :type id: str

    """
    return web.Response(status=200)


async def get_compute_cluster(request: web.Request, id) -> web.Response:
    """Get details for the compute cluster

    Get details for the compute cluster.

    :param id: ID of the compute cluster.
    :type id: str

    """
    return web.Response(status=200)


async def get_io_filters(request: web.Request, id) -> web.Response:
    """Get the ioFilters on the VMware compute cluster with a specific ID

    Get the summary of the ioFilters on the VMware compute cluster with a specific ID.

    :param id: ID of the VMware compute cluster.
    :type id: str

    """
    return web.Response(status=200)


async def install_io_filter(request: web.Request, id, body) -> web.Response:
    """Install the Rubrik ioFilter to the VMware cluster with a specific ID

    Install the latest version of Rubrik ioFilter to the VMware cluster with a specific ID. The cluster must be in maintenance mode to install the ioFilter successfully. The vCenter of the VMware compute cluster must be of version 6.7 and above.

    :param id: ID of the VMware compute cluster.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = FullyQualifiedDomainNameInfo.from_dict(body)
    return web.Response(status=200)


async def query_compute_cluster(request: web.Request, datacenter_id=None, primary_cluster_id=None, snappable_status=None) -> web.Response:
    """Get all the clusters belonging to this datacenter

    Get all the clusters belonging to this datacenter.

    :param datacenter_id: Filter clusters on data center ID.
    :type datacenter_id: str
    :param primary_cluster_id: Filter on a primary cluster ID. Also accepts value &#39;local&#39;.
    :type primary_cluster_id: str
    :param snappable_status: Determines whether to fetch Compute Clusters with additional privilege checks.
    :type snappable_status: str

    """
    return web.Response(status=200)


async def uninstall_io_filter(request: web.Request, id) -> web.Response:
    """Uninstall the Rubrik ioFilter from the VMware cluster with a specific ID

    Uninstall the Rubrik ioFilter from the VMware cluster with a specific ID. The cluster must be in maintenance mode to uninstall the ioFilter successfully. The vCenter of the VMware compute cluster must be of version 6.7 and above.

    :param id: ID of the VMware compute cluster.
    :type id: str

    """
    return web.Response(status=200)


async def update_compute_cluster(request: web.Request, id, body) -> web.Response:
    """Modify information for a VMware compute cluster

    Update the configuredSlaDomainId for a VMware compute cluster with a specific ID.

    :param id: ID of the compute cluster.
    :type id: str
    :param body: Object with changes for the Compute Cluster information.
    :type body: dict | bytes

    """
    body = ComputeClusterUpdate.from_dict(body)
    return web.Response(status=200)


async def upgrade_io_filter(request: web.Request, id, body) -> web.Response:
    """Upgrade the Rubrik ioFilter for the VMware cluster with a specific ID

    Upgrade the Rubrik ioFilter for a VMware cluster with a specific ID. The cluster must be in maintenance mode to upgrade the ioFilter successfully. The vCenter of the VMware compute cluster must be of version 6.7 and above.

    :param id: ID of the VMware compute cluster.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = FullyQualifiedDomainNameInfo.from_dict(body)
    return web.Response(status=200)
