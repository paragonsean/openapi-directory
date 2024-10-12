from typing import List, Dict
from aiohttp import web

from openapi_server.models.apply_legal_hold_definition import ApplyLegalHoldDefinition
from openapi_server.models.dissolve_legal_hold_definition import DissolveLegalHoldDefinition
from openapi_server.models.dissolve_legal_hold_response import DissolveLegalHoldResponse
from openapi_server.models.legal_hold_summary import LegalHoldSummary
from openapi_server.models.legal_hold_summary_list_response import LegalHoldSummaryListResponse
from openapi_server.models.object_hold_summary_list_response import ObjectHoldSummaryListResponse
from openapi_server import util


async def apply_legal_hold(request: web.Request, body) -> web.Response:
    """Apply a Legal Hold

    Places a snapshot on legal hold by specifying the hold requirements.

    :param body: 
    :type body: dict | bytes

    """
    body = ApplyLegalHoldDefinition.from_dict(body)
    return web.Response(status=200)


async def dissolve_legal_hold_snapshots(request: web.Request, id, body) -> web.Response:
    """Dissolve a collection of snapshots of specified data source from Legal Hold

    Dissolve a collection of snapshots of specified data source from Legal Hold.

    :param id: ID of the data source.
    :type id: str
    :param body: An object that contains the IDs of the snapshots to remove from legal hold status.
    :type body: dict | bytes

    """
    body = DissolveLegalHoldDefinition.from_dict(body)
    return web.Response(status=200)


async def get_legal_hold_objects(request: web.Request, object_id=None, limit=None, offset=None, object_name=None, object_type=None, sort_by=None, sort_order=None) -> web.Response:
    """Get objects part of Legal Hold

    Returns the object details for object with snapshots under legal hold.

    :param object_id: Limit the list to a particular object.
    :type object_id: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: Specifies a number of initial matches to ignore.
    :type offset: int
    :param object_name: Limits the list to objects that match a specified value for the object name.
    :type object_name: str
    :param object_type: Limits the list to objects that match a specified type.
    :type object_type: str
    :param sort_by: The attribute used to sort summary information. The optional parameter _sort_order_ specifies ascending or descending sort order.
    :type sort_by: str
    :param sort_order: Specifies ascending or descending sort order. Summary results are sorted in ascending order when this parameter is not specified.
    :type sort_order: str

    """
    return web.Response(status=200)


async def query_legal_hold(request: web.Request, object_id=None, limit=None, offset=None, object_name=None, object_type=None, before_date=None, after_date=None, placed_on_hold_before_date=None, placed_on_hold_after_date=None, sort_by=None, sort_order=None, snapshot_type=None) -> web.Response:
    """Get snasphots held under legal hold

    Get summary for snapshots under legal hold. If object_id is passed, return summary information only for snapshots of the object under legal hold else return summary for all snapshots under legal hold.

    :param object_id: Limit the list to snapshot for the particular object.
    :type object_id: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: An integer that specifies a number of initial matches to ignore.
    :type offset: int
    :param object_name: Limits the list to objects that match a specified value for the object name.
    :type object_name: str
    :param object_type: Limits the list to objects that match a specified type.
    :type object_type: str
    :param before_date: Limits the list to snapshots with holds created before a specified date.
    :type before_date: str
    :param after_date: Limits the list to snapshots with holds created after a specified date.
    :type after_date: str
    :param placed_on_hold_before_date: Limits the list to snapshots which were placed on legal hold before a specified date.
    :type placed_on_hold_before_date: str
    :param placed_on_hold_after_date: Limits the list to snapshots which were placed on legal hold after a specified date.
    :type placed_on_hold_after_date: str
    :param sort_by: The attribute used to sort summary information. The optional parameter **_sort_order_** specifies ascending or descending sort order.
    :type sort_by: str
    :param sort_order: Specifies ascending or descending sort order. Summary results are sorted in ascending order when this parameter is not specified.
    :type sort_order: str
    :param snapshot_type: Specifies the type of snapshots to be returned.
    :type snapshot_type: str

    """
    before_date = util.deserialize_datetime(before_date)
    after_date = util.deserialize_datetime(after_date)
    placed_on_hold_before_date = util.deserialize_datetime(placed_on_hold_before_date)
    placed_on_hold_after_date = util.deserialize_datetime(placed_on_hold_after_date)
    return web.Response(status=200)
