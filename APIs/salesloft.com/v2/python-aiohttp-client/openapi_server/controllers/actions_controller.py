from typing import List, Dict
from aiohttp import web

from openapi_server.models.action import Action
from openapi_server import util


async def v2_actions_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch an action

    Fetches an action, by ID only. This endpoint will only return actions that are in_progress or pending_activity. Once an action is complete, the request for that action will return a 404 status code. 

    :param id: Action ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_actions_json_get(request: web.Request, ids=None, step_id=None, type=None, due_on=None, user_guid=None, person_id=None, cadence_id=None, multitouch_group_id=None, updated_at=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List actions

    Fetches multiple action records. The records can be filtered, paged, and sorted according to the respective parameters. Only actions that are currently \&quot;in_progess\&quot; will be returned by this endpoint.  If the requester is not an admin, this endpoint will only return actions belonging to the requester. If the request is an admin, this endpoint will return actions for the entire team. Additionaly, an admin may use the user_guid parameter to request actions that belong to specific users on the team. 

    :param ids: IDs of actions to fetch.
    :type ids: List[int]
    :param step_id: Fetch actions by step ID
    :type step_id: int
    :param type: Filter actions by type
    :type type: str
    :param due_on: Equality filters that are applied to the due_on field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type due_on: List[str]
    :param user_guid: Filters actions by the user&#39;s guid. Multiple user guids can be applied. The user must be a team admin to filter other users&#39; actions
    :type user_guid: List[str]
    :param person_id: Filters actions by person_id. Multiple person ids can be applied
    :type person_id: List[int]
    :param cadence_id: Filters actions by cadence_id. Multiple cadence ids can be applied
    :type cadence_id: List[int]
    :param multitouch_group_id: Filters actions by multitouch_group_id. Multiple multitouch group ids can be applied
    :type multitouch_group_id: List[int]
    :param updated_at: Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type updated_at: List[str]
    :param sort_by: Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
    :type sort_by: str
    :param sort_direction: Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    :type sort_direction: str
    :param per_page: How many records to show per page in the range [1, 100]. Defaults to 25
    :type per_page: int
    :param page: The current page to fetch results from. Defaults to 1
    :type page: int
    :param include_paging_counts: Whether to include total_pages and total_count in the metadata. Defaults to false
    :type include_paging_counts: bool
    :param limit_paging_counts: Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    :type limit_paging_counts: bool

    """
    return web.Response(status=200)
