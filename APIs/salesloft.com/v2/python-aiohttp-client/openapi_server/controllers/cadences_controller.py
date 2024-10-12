from typing import List, Dict
from aiohttp import web

from openapi_server.models.cadence import Cadence
from openapi_server import util


async def v2_cadences_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch a cadence

    Fetches a cadence, by ID only. 

    :param id: Cadence ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_cadences_json_get(request: web.Request, ids=None, updated_at=None, team_cadence=None, shared=None, owned_by_guid=None, people_addable=None, name=None, group_ids=None, archived=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List cadences

    Fetches multiple cadence records. The records can be filtered, paged, and sorted according to the respective parameters. 

    :param ids: IDs of cadences to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param updated_at: Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type updated_at: List[str]
    :param team_cadence: Filters cadences by whether they are a team cadence or not
    :type team_cadence: bool
    :param shared: Filters cadences by whether they are shared
    :type shared: bool
    :param owned_by_guid: Filters cadences by the owner&#39;s guid. Multiple owner guids can be applied
    :type owned_by_guid: List[str]
    :param people_addable: Filters cadences by whether they are able to have people added to them
    :type people_addable: bool
    :param name: Filters cadences by name
    :type name: List[str]
    :param group_ids: Filters by group ids. Also supports group ids passed in as a JSON array string
    :type group_ids: str
    :param archived: Filters by whether the Cadences have been archived. Excluding this field will result in both archived and unarchived Cadences to return.
    :type archived: bool
    :param sort_by: Key to sort on, must be one of: created_at, updated_at, name. Defaults to updated_at
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
