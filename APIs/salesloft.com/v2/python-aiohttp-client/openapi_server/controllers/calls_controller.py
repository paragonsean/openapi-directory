from typing import List, Dict
from aiohttp import web

from openapi_server.models.call import Call
from openapi_server import util


async def v2_activities_calls_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch a call

    Fetches a call, by ID only. 

    :param id: Call ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_activities_calls_json_get(request: web.Request, ids=None, created_at=None, updated_at=None, user_guid=None, person_id=None, sentiment=None, disposition=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List calls

    Fetches multiple call records. The records can be filtered, paged, and sorted according to the respective parameters. 

    :param ids: IDs of calls to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param created_at: Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type created_at: List[str]
    :param updated_at: Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type updated_at: List[str]
    :param user_guid: Filters list to only include guids
    :type user_guid: List[str]
    :param person_id: Filters calls by person_id. Multiple person ids can be applied
    :type person_id: List[int]
    :param sentiment: Filters calls by sentiment. Sentiment matches are exact and case sensitive. Multiple sentiments are allowed.
    :type sentiment: List[str]
    :param disposition: Filters calls by disposition. Disposition matches are exact and case sensitive. Multiple dispositions are allowed.
    :type disposition: List[str]
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


async def v2_activities_calls_json_post(request: web.Request, person_id, action_id=None, crm_params=None, disposition=None, duration=None, linked_call_data_record_ids=None, notes=None, sentiment=None, to=None, user_guid=None) -> web.Response:
    """Create a call

    Creates a call. The parameters of this endpoint can be used to create an action and ensure that the CRM Task is mapped correctly. 

    :param person_id: The ID of the person whom this call will be logged for
    :type person_id: int
    :param action_id: Action that this call is being logged for. This will validate that the action is still valid before completing it. The same action can never be successfully passed twice to this endpoint. The action must have a type of &#39;phone&#39;. 
    :type action_id: int
    :param crm_params: CRM specific parameters. Some parameters are required on a per-team basis. Consume the CrmActivityFields endpoint to receive a list of valid parameters. The \\\&quot;field\\\&quot; property is passed as the key of this object, and the value of this object is the value that you would like to set.  If CrmActivityField has a non-null value, then that value must be submitted, or excluded from API calls, as these values are automatically applied. 
    :type crm_params: dict | bytes
    :param disposition: The disposition of the call. Can be required on a per-team basis. Must be present in the disposition list.
    :type disposition: str
    :param duration: The length of the call, in seconds
    :type duration: int
    :param linked_call_data_record_ids: CallDataRecord associations that will become linked to the created call. It is possible to pass multiple CallDataRecord ids in this field; this can be used to represent multiple phone calls that made up a single call.  Any call data record that is used must not already be linked to a call. It is not possible to link a call data record to multiple calls, and it is not possible to re-assign a call data record to a different call. 
    :type linked_call_data_record_ids: List[int]
    :param notes: Notes to log for the call. This is similar to the notes endpoint, but ensures that the notes get synced to the user&#39;s CRM
    :type notes: str
    :param sentiment: The sentiment of the call. Can be required on a per-team basis. Must be present in the sentiment list.
    :type sentiment: str
    :param to: The phone number that was called
    :type to: str
    :param user_guid: Guid of the user whom this call should be logged for. Defaults to the authenticated user. Only team admins can pass another user&#39;s guid
    :type user_guid: str

    """
    crm_params = object.from_dict(crm_params)
    return web.Response(status=200)
