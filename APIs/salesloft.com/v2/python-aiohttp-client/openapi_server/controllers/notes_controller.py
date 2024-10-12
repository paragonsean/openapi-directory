from typing import List, Dict
from aiohttp import web

from openapi_server.models.note import Note
from openapi_server.models.person import Person
from openapi_server import util


async def v2_notes_id_json_delete(request: web.Request, id) -> web.Response:
    """Delete a note

    Deletes a note owned by authorized account. This operation is not reversible without contacting support. This operation can be called multiple times successfully. 

    :param id: Note ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_notes_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch a note

    Fetches a note, by ID only. 

    :param id: Note ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_notes_id_json_put(request: web.Request, id, content, call_id=None) -> web.Response:
    """Update a note

    Updates a note. Any changes to the note or associated records will not reflect in your CRM. 

    :param id: Note ID
    :type id: str
    :param content: The content of the note
    :type content: str
    :param call_id: ID of the call with which the note is associated. The call cannot already have a note. If the note is associated to a call already, it will become associated to the requested call
    :type call_id: int

    """
    return web.Response(status=200)


async def v2_notes_json_get(request: web.Request, associated_with_type=None, associated_with_id=None, updated_at=None, ids=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List notes

    Fetches multiple note records. The records can be filtered, paged, and sorted according to the respective parameters. 

    :param associated_with_type: Case insensitive type of item with which the note is associated.  Value must be one of: person, account
    :type associated_with_type: str
    :param associated_with_id: ID of the item with which the note is associated.  The associated_with_type must also be present if this parameter is used
    :type associated_with_id: int
    :param updated_at: Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type updated_at: List[str]
    :param ids: IDs of notes to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
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


async def v2_notes_json_post(request: web.Request, associated_with_id, associated_with_type, content, call_id=None, skip_crm_sync=None, subject=None, user_guid=None) -> web.Response:
    """Create a note

    Creates a note. 

    :param associated_with_id: ID of the item with which the note is associated
    :type associated_with_id: int
    :param associated_with_type: Case insensitive type of item with which the note is associated.  Value must be one of: person, account
    :type associated_with_type: str
    :param content: The content of the note
    :type content: str
    :param call_id: ID of the call with which the note is associated. The call cannot already have a note
    :type call_id: int
    :param skip_crm_sync: Boolean indicating if the CRM sync should be skipped.  No syncing will occur if true
    :type skip_crm_sync: bool
    :param subject: The subject of the note&#39;s crm activity, defaults to &#39;Note&#39;
    :type subject: str
    :param user_guid: The user to create the note for. Only team admins may create notes on behalf of other users. Defaults to the requesting user
    :type user_guid: str

    """
    return web.Response(status=200)
