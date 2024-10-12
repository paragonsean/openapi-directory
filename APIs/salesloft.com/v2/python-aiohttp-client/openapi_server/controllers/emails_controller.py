from typing import List, Dict
from aiohttp import web

from openapi_server.models.email import Email
from openapi_server import util


async def v2_activities_emails_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch an email

    Fetches an email, by ID only. 

    :param id: Email ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_activities_emails_json_get(request: web.Request, ids=None, updated_at=None, bounced=None, crm_activity_id=None, action_id=None, user_id=None, status=None, cadence_id=None, step_id=None, one_off=None, scoped_fields=None, person_id=None, email_addresses=None, personalization=None, sent_at=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List emails

    Fetches multiple email records. The records can be filtered, paged, and sorted according to the respective parameters. 

    :param ids: IDs of emails to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param updated_at: Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type updated_at: List[str]
    :param bounced: Filters emails by whether they have bounced or not
    :type bounced: bool
    :param crm_activity_id: Filters emails by crm_activity_id. Multiple crm activty ids can be applied
    :type crm_activity_id: List[int]
    :param action_id: Filters emails by action_id. Multiple action ids can be applied
    :type action_id: List[int]
    :param user_id: Filters emails by user_id. Multiple User ids can be applied
    :type user_id: List[int]
    :param status: Filters emails by status. Multiple status can be applied, possible values are sent, sent_from_gmail, sent_from_external, pending, pending_reply_check, scheduled, sending, delivering, failed, cancelled, pending_through_gmail, pending_through_external
    :type status: List[str]
    :param cadence_id: Filters emails by cadence. Multiple cadence ids can be applied
    :type cadence_id: List[int]
    :param step_id: Filters emails by step. Multiple step ids can be applied
    :type step_id: List[int]
    :param one_off: Filters emails by one-off only
    :type one_off: bool
    :param scoped_fields: Specify explicit scoped fields desired on the Email Resource.
    :type scoped_fields: List[str]
    :param person_id: Filters emails by person_id. Multiple person ids can be applied
    :type person_id: List[int]
    :param email_addresses: Filters emails by recipient email address. Multiple emails can be applied.
    :type email_addresses: List[str]
    :param personalization: Filters emails by personalization score
    :type personalization: List[str]
    :param sent_at: Equality filters that are applied to the sent_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type sent_at: List[str]
    :param sort_by: Key to sort on, must be one of: updated_at, send_time. Defaults to updated_at
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
