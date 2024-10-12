from typing import List, Dict
from aiohttp import web

from openapi_server.models.host_hierarchy_object_summary import HostHierarchyObjectSummary
from openapi_server.models.host_hierarchy_object_summary_list_response import HostHierarchyObjectSummaryListResponse
from openapi_server import util


async def get_host_hierarchy_children(request: web.Request, id, name=None, object_type=None, effective_sla_domain_id=None, primary_cluster_id=None, sla_assignment=None, template_id=None, vendor_type=None, export_point=None, operating_system_type=None, sort_by=None, sort_order=None, limit=None, offset=None) -> web.Response:
    """Get immediate descendant objects

    Retrieve the list of immediate descendant objects for the specified parent.

    :param id: ID of the parent host hierarchy object. To get top-level nodes, use **root** as the ID.
    :type id: str
    :param name: Search object by object name.
    :type name: str
    :param object_type: Filter by node object type.
    :type object_type: str
    :param effective_sla_domain_id: Filter by ID of effective SLA domain.
    :type effective_sla_domain_id: str
    :param primary_cluster_id: Filter by primary cluster ID, or **local**.
    :type primary_cluster_id: str
    :param sla_assignment: Limit a response to the results that have the specified SLA Domain assignment type.
    :type sla_assignment: str
    :param template_id: Filter by fileset template ID.
    :type template_id: str
    :param vendor_type: Filter by NAS vendor.
    :type vendor_type: str
    :param export_point: Search object by export point.
    :type export_point: str
    :param operating_system_type: Filter the summary information based on the operating system type. Accepted values are &#39;Windows&#39;, &#39;UnixLike&#39;, &#39;ANY&#39;, &#39;NONE&#39;. Use **_NONE_** to only return information for hosts templates that do not have operating system type set. Use **_ANY_** to only return information for hosts that have operating system type set.
    :type operating_system_type: str
    :param sort_by: Attribute to sort the results on.
    :type sort_by: str
    :param sort_order: Order for sorting the results, either ascending or descending.
    :type sort_order: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: Number of matches to ignore from the beginning of the results.
    :type offset: int

    """
    return web.Response(status=200)


async def get_host_hierarchy_object(request: web.Request, id) -> web.Response:
    """Get summary of a host/share hierarchy object

    Retrieve details for the specified object in the host/share hierarchy. 

    :param id: ID of the host hierarchy object.
    :type id: str

    """
    return web.Response(status=200)
