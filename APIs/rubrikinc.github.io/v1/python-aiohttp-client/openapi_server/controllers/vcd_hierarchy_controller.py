from typing import List, Dict
from aiohttp import web

from openapi_server.models.vcd_hierarchy_object_summary import VcdHierarchyObjectSummary
from openapi_server.models.vcd_hierarchy_object_summary_list_response import VcdHierarchyObjectSummaryListResponse
from openapi_server import util


async def get_vcd_hierarchy_children_v1(request: web.Request, id, sort_by=None, sort_order=None, limit=None, offset=None, name=None, is_relic=None, effective_sla_domain_id=None, object_type=None, primary_cluster_id=None, sla_assignment=None, snappable_status=None) -> web.Response:
    """Get immediate descendant objects

    Retrieve the list of immediate descendant objects for the specified parent.

    :param id: ID of the parent vCD hierarchy object. To get top-level nodes, use **root** as the ID.
    :type id: str
    :param sort_by: Attribute to sort the results on.
    :type sort_by: str
    :param sort_order: Order for sorting the results, either ascending or descending.
    :type sort_order: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: Number of matches to ignore from the beginning of the results.
    :type offset: int
    :param name: Search object by object name.
    :type name: str
    :param is_relic: Filter by isRelic field of vCD vApp hierarchy object. Return both relic and non-relic children when this value is not specified.
    :type is_relic: bool
    :param effective_sla_domain_id: Filter by ID of effective SLA domain.
    :type effective_sla_domain_id: str
    :param object_type: Filter by node object type.
    :type object_type: str
    :param primary_cluster_id: Filter by primary cluster ID, or **local**.
    :type primary_cluster_id: str
    :param sla_assignment: Filter by SLA assignment type.
    :type sla_assignment: str
    :param snappable_status: Filters vCD hierarchy objects based on the specified query value.
    :type snappable_status: str

    """
    return web.Response(status=200)


async def get_vcd_hierarchy_descendants_v1(request: web.Request, id, sort_by=None, sort_order=None, limit=None, offset=None, name=None, is_relic=None, effective_sla_domain_id=None, object_type=None, primary_cluster_id=None, sla_assignment=None, snappable_status=None) -> web.Response:
    """Get list of descendant objects

    Retrieve the list of descendant objects for the specified parent.

    :param id: ID of the parent vCD hierarchy object. To get top-level nodes, use **root** as the ID.
    :type id: str
    :param sort_by: Attribute to sort the results on.
    :type sort_by: str
    :param sort_order: Order for sorting the results, either ascending or descending.
    :type sort_order: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: Ignore these many matches in the beginning.
    :type offset: int
    :param name: Search object by object name.
    :type name: str
    :param is_relic: Filter by isRelic field of vCD vApp hierarchy object. Return both relic and non-relic descendants if this query is not set.
    :type is_relic: bool
    :param effective_sla_domain_id: Filter by ID of effective SLA domain.
    :type effective_sla_domain_id: str
    :param object_type: Filter by node object type.
    :type object_type: str
    :param primary_cluster_id: Filter by primary cluster ID, or **local**.
    :type primary_cluster_id: str
    :param sla_assignment: Filter by SLA assignment type.
    :type sla_assignment: str
    :param snappable_status: Filters vCD hierarchy objects based on the specified query value.
    :type snappable_status: str

    """
    return web.Response(status=200)


async def get_vcd_hierarchy_object_v1(request: web.Request, id) -> web.Response:
    """Get summary of a vCD hierarchy object

    Retrieve details for the specified object in the vCD hierarchy.

    :param id: ID of the vCD hierarchy object.
    :type id: str

    """
    return web.Response(status=200)
