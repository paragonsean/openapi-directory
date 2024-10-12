from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_history import ActivityHistory
from openapi_server import util


async def v2_activity_histories_get(request: web.Request, per_page=None, page=None, include_paging_counts=None, sort_by=None, sort_direction=None, type=None, resource=None, occurred_at=None, pinned=None, resource_type=None, resource_id=None, updated_at=None, user_guid=None) -> web.Response:
    """List Past Activities

    Fetches all of the customer&#39;s past activities for your application. Returns all the Activities that are found on the Salesloft Activity Feed. &lt;a href&#x3D;\&quot;/activity-history.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;Visit here for more details&lt;/a&gt;.

    :param per_page: How many records to show per page in the range [1, 100]. Defaults to 25
    :type per_page: int
    :param page: The current page to fetch results from. Defaults to 1
    :type page: int
    :param include_paging_counts: Whether to include total_pages and total_count in the metadata. Defaults to false
    :type include_paging_counts: bool
    :param sort_by: Key to sort on, must be one of: occurred_at, updated_at. Defaults to occurred_at
    :type sort_by: str
    :param sort_direction: Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    :type sort_direction: str
    :param type: Filter by the type of activity. Must be one of: added_to_cadence, completed_action, call, requested_email, sent_email, received_email, email_reply, note, success, dnc_event, residency_change, meeting, meeting_held, message_conversation, task, voicemail, opportunity_stage_change, opportunity_amount_change, opportunity_close_date_change. Can be provided as an array, or as an object of type[resource_type][]&#x3D;type
    :type type: str
    :param resource: For internal use only. This field does not comply with our backwards compatibility policies. This filter is for authenticated users of Salesloft only and will not work for OAuth Applications. Filter by the {resource_type, resource_id} of activity. Provide this in the format resource[]&#x3D;person,1234
    :type resource: str
    :param occurred_at: Equality filters that are applied to the occurred_at field. A single filter can be used by itself or combined with other filters to create a range. ---CUSTOM--- {\&quot;keys\&quot;:[{\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;},{\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;},{\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;},{\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;}],\&quot;type\&quot;:\&quot;object\&quot;} 
    :type occurred_at: dict | bytes
    :param pinned: Filter by the pinned status of activity. Must be &#39;true&#39; or &#39;false&#39;
    :type pinned: bool
    :param resource_type: Filter by the resource type. A resource is a Salesloft object that the activity is attributed to. A valid resource types must be one of person, account, crm_opportunity. Can be provided as an array
    :type resource_type: str
    :param resource_id: Filter by the resource id. \&quot;resource_type\&quot; filter is required to use this filter.
    :type resource_id: List[str]
    :param updated_at: Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range. ---CUSTOM--- {\&quot;keys\&quot;:[{\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;},{\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;},{\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;},{\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;}],\&quot;type\&quot;:\&quot;object\&quot;} 
    :type updated_at: dict | bytes
    :param user_guid: Filter activities by a user&#39;s guid.
    :type user_guid: str

    """
    occurred_at = .from_dict(occurred_at)
    updated_at = .from_dict(updated_at)
    return web.Response(status=200)
