from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.bulk_tier_snapshots_config import BulkTierSnapshotsConfig
from openapi_server.models.managed_object_pending_sla_info import ManagedObjectPendingSlaInfo
from openapi_server.models.snapshot_summary_list_response import SnapshotSummaryListResponse
from openapi_server.models.unmanaged_object_details_list_response import UnmanagedObjectDetailsListResponse
from openapi_server.models.unmanaged_object_sla_assignment_info import UnmanagedObjectSlaAssignmentInfo
from openapi_server.models.unmanaged_object_summary_list_response import UnmanagedObjectSummaryListResponse
from openapi_server import util


async def assign_to_retention_sla_async(request: web.Request, body) -> web.Response:
    """Assign relic/unmanaged entities to an SLA Domain for managing retention asynchronously

    Assign relic/unmanaged entities to the specified SLA Domain for managing retention. The assignment event runs asynchronously.

    :param body: Object with SLA Domain ID and a comma-separated list of the IDs of the relic/unmanaged entities being assigned to the SLA Domain.
    :type body: dict | bytes

    """
    body = UnmanagedObjectSlaAssignmentInfo.from_dict(body)
    return web.Response(status=200)


async def bulk_tier_existing_snapshots(request: web.Request, body) -> web.Response:
    """Bulk tier existing snapshots to cold storage

    Schedules a job to tier existing snapshots of the specified objects to cold storage.

    :param body: A list of object IDs to tier. Optionally specifies a location ID.
    :type body: dict | bytes

    """
    body = BulkTierSnapshotsConfig.from_dict(body)
    return web.Response(status=200)


async def query_unmanaged_object_snapshots_v1(request: web.Request, id, limit=None, offset=None, search_value=None, snapshot_type=None, before_date=None, after_date=None, sort_by=None, sort_order=None) -> web.Response:
    """Get summary of all the snapshots for a given object

    Gets summary information for all snapshots of the object with the specified object ID.

    :param id: ID of a object.
    :type id: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: Ignore these many matches in the beginning.
    :type offset: int
    :param search_value: Search snapshot by date and time.
    :type search_value: str
    :param snapshot_type: Filter by snapshot type. Valid types are OnDemand, PolicyBased, Retrieved.
    :type snapshot_type: str
    :param before_date: Filter all the snapshots before a date.
    :type before_date: str
    :param after_date: Filter all the snapshots after a date.
    :type after_date: str
    :param sort_by: Sort by given attribute.
    :type sort_by: str
    :param sort_order: The sort order. The default sort order is ascending.
    :type sort_order: str

    """
    before_date = util.deserialize_datetime(before_date)
    after_date = util.deserialize_datetime(after_date)
    return web.Response(status=200)


async def query_unmanaged_object_v1(request: web.Request, limit=None, after_id=None, search_value=None, unmanaged_status=None, object_type=None, sort_by=None, sort_order=None) -> web.Response:
    """Get summary of all the objects with unmanaged snapshots

    Get summary of all the objects with unmanaged snapshots.

    :param limit: Limit the number of matches returned.
    :type limit: int
    :param after_id: First unmanaged object after which objects should be retrieved.
    :type after_id: str
    :param search_value: Filters by the object name using infix search.
    :type search_value: str
    :param unmanaged_status: Filters by object status. Valid status are Protected, Unprotected, and Relic.
    :type unmanaged_status: str
    :param object_type: Filter by the type of the unmanaged object.
    :type object_type: str
    :param sort_by: Sort the result by given attribute.
    :type sort_by: str
    :param sort_order: The sort order. The default sort order is ascending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def query_unmanaged_reader_object(request: web.Request, limit=None, after_id=None, object_name=None, unmanaged_status=None, object_type=None, sort_by=None, sort_order=None) -> web.Response:
    """Get summary of all unmanaged reader objects

    A summary of all unmanaged objects recovered from reader archival locations.

    :param limit: Limit the number of matches returned.
    :type limit: int
    :param after_id: Retrieve objects after the unmanaged object with the specified ID.
    :type after_id: str
    :param object_name: Search object by object name.
    :type object_name: str
    :param unmanaged_status: Filters by object status. Valid status are Protected, Unprotected, and Relic.
    :type unmanaged_status: str
    :param object_type: Filter by the type of the unmanaged object.
    :type object_type: str
    :param sort_by: Sort the result by given attribute.
    :type sort_by: str
    :param sort_order: The sort order. The default sort order is ascending.
    :type sort_order: str

    """
    return web.Response(status=200)
