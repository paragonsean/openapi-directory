from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_sla_conflicts_summary import BulkSlaConflictsSummary
from openapi_server.models.hierarchy_object_ids import HierarchyObjectIds
from openapi_server import util


async def bulk_hierarchy_sla_conflicts_v1(request: web.Request, body) -> web.Response:
    """Retrieve the list of descendant objects with SLA conflicts in bulk

    Retrieve the list of descendant objects with an explicitly configured SLA domain, or inherit an SLA domain from a different parent for each managed ID.

    :param body: List of hierarchy object IDs.
    :type body: dict | bytes

    """
    body = HierarchyObjectIds.from_dict(body)
    return web.Response(status=200)
