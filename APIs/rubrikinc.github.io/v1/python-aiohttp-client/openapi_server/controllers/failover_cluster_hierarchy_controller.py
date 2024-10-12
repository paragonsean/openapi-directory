from typing import List, Dict
from aiohttp import web

from openapi_server.models.failover_cluster_hierarchy_object_summary import FailoverClusterHierarchyObjectSummary
from openapi_server.models.failover_cluster_hierarchy_object_summary_list_response import FailoverClusterHierarchyObjectSummaryListResponse
from openapi_server import util


async def get_failover_cluster_hierarchy_children(request: web.Request, id, name=None, operating_system_type=None, object_type=None, primary_cluster_id=None, limit=None, offset=None, configured_sla_domain_id=None, sla_assignment=None, sort_by=None, sort_order=None) -> web.Response:
    """Get list of immediate descendant objects

    Retrieve the list of immediate descendant objects for the specified parent.

    :param id: ID of the parent failover cluster hierarchy object. To get top-level nodes, use **root** as the ID.
    :type id: str
    :param name: Filter a response by making an infix comparison of the failover cluster name or failover cluster app name.
    :type name: str
    :param operating_system_type: Filter a response based on the failover cluster operating system type.
    :type operating_system_type: str
    :param object_type: Filter by node object type.
    :type object_type: str
    :param primary_cluster_id: Filter by primary cluster ID, or **local**.
    :type primary_cluster_id: str
    :param limit: An integer that specifies the maximum number of matches to return.
    :type limit: int
    :param offset: An integer that specifies a number of initial matches to ignore.
    :type offset: int
    :param configured_sla_domain_id: Filter by configured SLA domain.
    :type configured_sla_domain_id: str
    :param sla_assignment: Filter by SLA assignment type.
    :type sla_assignment: str
    :param sort_by: Attribute to sort the results on.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def get_failover_cluster_hierarchy_descendants(request: web.Request, id, name=None, operating_system_type=None, object_type=None, primary_cluster_id=None, limit=None, offset=None, configured_sla_domain_id=None, sla_assignment=None, sort_by=None, sort_order=None) -> web.Response:
    """Get list of descendant objects

    Retrieve the list of descendant objects for the specified parent.

    :param id: ID of the parent failover cluster hierarchy object. To get top-level nodes, use **root** as the ID.
    :type id: str
    :param name: Filter a response by making an infix comparison of the failover cluster name or failover cluster app name.
    :type name: str
    :param operating_system_type: Filter a response based on the failover cluster operating system type.
    :type operating_system_type: str
    :param object_type: Filter by node object type.
    :type object_type: str
    :param primary_cluster_id: Filter by primary cluster ID, or **local**.
    :type primary_cluster_id: str
    :param limit: An integer that specifies the maximum number of matches to return.
    :type limit: int
    :param offset: An integer that specifies a number of initial matches to ignore.
    :type offset: int
    :param configured_sla_domain_id: Filter by configured SLA domain.
    :type configured_sla_domain_id: str
    :param sla_assignment: Filter by SLA assignment type.
    :type sla_assignment: str
    :param sort_by: Attribute to sort the results on.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def get_failover_cluster_hierarchy_object(request: web.Request, id) -> web.Response:
    """Get summary of a hierarchy object

    Retrieve details for the specified hierarchy object.

    :param id: ID of the hierarchy object.
    :type id: str

    """
    return web.Response(status=200)
