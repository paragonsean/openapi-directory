from typing import List, Dict
from aiohttp import web

from openapi_server.models.meeting import Meeting
from openapi_server import util


async def v2_meetings_id_json_put(request: web.Request, id, event_id=None, i_cal_uid=None, no_show=None, reschedule_status=None, status=None) -> web.Response:
    """Update a meeting

    Updates a meeting, by ID only. 

    :param id: Meeting ID
    :type id: str
    :param event_id: Meeting ID from the calendar provider
    :type event_id: str
    :param i_cal_uid: Meeting unique identifier (iCalUID)
    :type i_cal_uid: str
    :param no_show: Whether the meeting is a No Show meeting
    :type no_show: bool
    :param reschedule_status: Status of the meeting rescheduling progress. Possible values are: pending, booked, failed, retry
    :type reschedule_status: str
    :param status: Status of the meeting creation progress. Possible values are: pending, booked, failed, retry
    :type status: str

    """
    return web.Response(status=200)


async def v2_meetings_json_get(request: web.Request, ids=None, status=None, person_id=None, account_id=None, person_ids=None, event_ids=None, i_cal_uids=None, task_ids=None, include_meetings_settings=None, start_time=None, created_at=None, user_guids=None, show_deleted=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List meetings

    Fetches multiple meeting records. The records can be filtered, paged, and sorted according to the respective parameters. Meetings resource is responsible for events created via the Salesloft platform using calendaring features. These events can relate to cadences, people, and accounts. 

    :param ids: IDs of meetings to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param status: Filters meetings by status. Possible values are: pending, booked, failed, retry
    :type status: str
    :param person_id: Filters meetings by person_id. Multiple person ids can be applied
    :type person_id: str
    :param account_id: Filters meetings by account_id. Multiple account ids can be applied
    :type account_id: str
    :param person_ids: Filters meetings by person_id. Multiple person ids can be applied
    :type person_ids: List[int]
    :param event_ids: List of event IDs. If both event_ids and i_cal_uids params are passed, this filters will be ORed. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type event_ids: List[str]
    :param i_cal_uids: List of UIDs provided by calendar provider. If both event_ids and i_cal_uids params are passed, this filters will be ORed. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type i_cal_uids: List[str]
    :param task_ids: Filters meetings by task_id. Multiple task ids can be applied
    :type task_ids: List[int]
    :param include_meetings_settings: Flag to indicate whether to include owned_by_meetings_settings and booked_by_meetings_settings objects
    :type include_meetings_settings: bool
    :param start_time: Equality filters that are applied to the start_time field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type start_time: List[str]
    :param created_at: Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type created_at: List[str]
    :param user_guids: Filters meetings by user_guid. Multiple user guids can be applied
    :type user_guids: List[str]
    :param show_deleted: Whether to include deleted events in the result
    :type show_deleted: bool
    :param sort_by: Key to sort on, must be one of: start_time, created_at, updated_at. Defaults to start_time
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
