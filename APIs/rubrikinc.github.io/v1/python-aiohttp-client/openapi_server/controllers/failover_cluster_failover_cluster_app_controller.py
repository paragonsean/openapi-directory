from typing import List, Dict
from aiohttp import web

from openapi_server.models.failover_cluster_app_config import FailoverClusterAppConfig
from openapi_server.models.failover_cluster_app_detail import FailoverClusterAppDetail
from openapi_server.models.failover_cluster_app_summary import FailoverClusterAppSummary
from openapi_server.models.failover_cluster_app_summary_list_response import FailoverClusterAppSummaryListResponse
from openapi_server import util


async def bulk_delete_failover_cluster_app(request: web.Request, ids, preserve_snapshots=None) -> web.Response:
    """Delete failover cluster applications

    Delete failover cluster applications from Rubrik cluster.

    :param ids: The ID of each failover cluster application to delete.
    :type ids: List[str]
    :param preserve_snapshots: Specifies whether to preserve the snapshots of the fileset that belongs to a failover cluster application. When this value is &#39;true,&#39; the snapshots are preserved. The default value is &#39;true&#39;.
    :type preserve_snapshots: bool

    """
    return web.Response(status=200)


async def create_failover_cluster_app(request: web.Request, body) -> web.Response:
    """Create a failover cluster app

    Create a failover cluster app.

    :param body: Create configuration parameters for a failover cluster app.
    :type body: dict | bytes

    """
    body = FailoverClusterAppConfig.from_dict(body)
    return web.Response(status=200)


async def delete_failover_cluster_app(request: web.Request, id, preserve_snapshots=None) -> web.Response:
    """Delete a failover cluster app

    Delete a failover cluster app.

    :param id: ID of the failover cluster app.
    :type id: str
    :param preserve_snapshots: A Boolean that specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is &#39;true,&#39; the snapshots are preserved. The default value is &#39;true&#39;.
    :type preserve_snapshots: bool

    """
    return web.Response(status=200)


async def get_failover_cluster_app(request: web.Request, id) -> web.Response:
    """Get details of a failover cluster app

    Get details of a failover cluster app.

    :param id: ID of the failover cluster app.
    :type id: str

    """
    return web.Response(status=200)


async def query_failover_cluster_app(request: web.Request, name=None, sla_assignment=None, primary_cluster_id=None, operating_system_type=None, limit=None, offset=None, sort_by=None, sort_order=None) -> web.Response:
    """Get a summary of all failover cluster apps

    Get a summary of all failover cluster apps.

    :param name: Filter the response by comparing the failover cluster app name with the specified value.
    :type name: str
    :param sla_assignment: Limit a response to the results that have the specified SLA Domain assignment type.
    :type sla_assignment: str
    :param primary_cluster_id: Limit a response to the results that have the specified primary cluster value.
    :type primary_cluster_id: str
    :param operating_system_type: Filter a response based on the failover cluster operating system type.
    :type operating_system_type: str
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


async def update_failover_cluster_app(request: web.Request, id, body) -> web.Response:
    """Update a failover cluster app

    Update the failover cluster app with specified properties.

    :param id: ID of failover cluster app.
    :type id: str
    :param body: Properties to update.
    :type body: dict | bytes

    """
    body = FailoverClusterAppConfig.from_dict(body)
    return web.Response(status=200)
