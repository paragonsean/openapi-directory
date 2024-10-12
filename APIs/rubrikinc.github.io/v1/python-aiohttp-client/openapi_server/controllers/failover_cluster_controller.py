from typing import List, Dict
from aiohttp import web

from openapi_server.models.failover_cluster_config import FailoverClusterConfig
from openapi_server.models.failover_cluster_detail import FailoverClusterDetail
from openapi_server.models.failover_cluster_summary_list_response import FailoverClusterSummaryListResponse
from openapi_server import util


async def bulk_delete_failover_cluster(request: web.Request, ids, preserve_snapshots=None) -> web.Response:
    """Delete the provided failover clusters

    Delete the provided failover clusters.

    :param ids: The ID of each failover cluster to delete.
    :type ids: List[str]
    :param preserve_snapshots: Specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is &#39;true,&#39; the snapshots are preserved. The default value is &#39;true&#39;.
    :type preserve_snapshots: bool

    """
    return web.Response(status=200)


async def create_failover_cluster(request: web.Request, body) -> web.Response:
    """Create a failover cluster

    Create a failover cluster.

    :param body: Create configuration parameters for a failover cluster.
    :type body: dict | bytes

    """
    body = FailoverClusterConfig.from_dict(body)
    return web.Response(status=200)


async def delete_failover_cluster(request: web.Request, id, preserve_snapshots=None) -> web.Response:
    """Delete a failover cluster

    Delete a failover cluster.

    :param id: ID of the failover cluster.
    :type id: str
    :param preserve_snapshots: A Boolean that specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is &#39;true,&#39; the snapshots are preserved. The default value is &#39;true&#39;.
    :type preserve_snapshots: bool

    """
    return web.Response(status=200)


async def get_failover_cluster(request: web.Request, id) -> web.Response:
    """Get details of a failover cluster

    Get details of a failover cluster.

    :param id: ID of the failover cluster.
    :type id: str

    """
    return web.Response(status=200)


async def query_failover_cluster(request: web.Request, name=None, operating_system_type=None, sla_assignment=None, primary_cluster_id=None, limit=None, offset=None, sort_by=None, sort_order=None) -> web.Response:
    """Get a summary of all failover clusters

    Get a summary of all failover clusters.

    :param name: Filter a response by making an infix comparison of the failover cluster name in the response, with the specified value.
    :type name: str
    :param operating_system_type: Filter a response based on the operating system type.
    :type operating_system_type: str
    :param sla_assignment: Limit a response to the results that have the specified SLA Domain assignment type.
    :type sla_assignment: str
    :param primary_cluster_id: Limit a response to the results that have the specified primary cluster value.
    :type primary_cluster_id: str
    :param limit: Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort.
    :type limit: int
    :param offset: Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results.
    :type offset: int
    :param sort_by: Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def update_failover_cluster(request: web.Request, id, body) -> web.Response:
    """Update a failover cluster

    Update failover cluster with specified properties.

    :param id: ID of failover cluster.
    :type id: str
    :param body: Properties to update.
    :type body: dict | bytes

    """
    body = FailoverClusterConfig.from_dict(body)
    return web.Response(status=200)
