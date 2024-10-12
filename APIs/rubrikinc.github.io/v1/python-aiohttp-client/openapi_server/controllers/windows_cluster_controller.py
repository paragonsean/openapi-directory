from typing import List, Dict
from aiohttp import web

from openapi_server.models.windows_cluster_detail import WindowsClusterDetail
from openapi_server.models.windows_cluster_summary_list_response import WindowsClusterSummaryListResponse
from openapi_server import util


async def get_windows_cluster(request: web.Request, id) -> web.Response:
    """Get detailed information for a Windows cluster

    Returns a detailed view of a Windows server failover cluster.

    :param id: ID of the Windows cluster.
    :type id: str

    """
    return web.Response(status=200)


async def query_windows_cluster(request: web.Request, primary_cluster_id=None, is_agentless=None, snappable_status=None) -> web.Response:
    """Get summary information for Windows clusters

    Returns a list of summary information for Windows server failover clusters.

    :param primary_cluster_id: Filter by primary_cluster_id. Use **local** for the local cluster.
    :type primary_cluster_id: str
    :param is_agentless: Filter by is_agentless flag.
    :type is_agentless: bool
    :param snappable_status: Determines whether Windows clusters are fetched with additional privilege checks.
    :type snappable_status: str

    """
    return web.Response(status=200)
