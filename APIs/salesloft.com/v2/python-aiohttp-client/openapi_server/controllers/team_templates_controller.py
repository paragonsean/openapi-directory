from typing import List, Dict
from aiohttp import web

from openapi_server.models.team_template import TeamTemplate
from openapi_server import util


async def v2_team_templates_id_json_get(request: web.Request, id, include_signature=None) -> web.Response:
    """Fetch a team template

    Fetches a team template, by ID only. 

    :param id: Team Template ID
    :type id: str
    :param include_signature: Optionally will return the templates with the current user&#39;s email signature
    :type include_signature: bool

    """
    return web.Response(status=200)


async def v2_team_templates_json_get(request: web.Request, ids=None, updated_at=None, search=None, tag_ids=None, tag=None, include_archived_templates=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List team templates

    Fetches multiple team template records. The records can be filtered, paged, and sorted according to the respective parameters.  Team templates are templates that are available team-wide. Admins may use team templates to create original content for the entire team, monitor version control to ensure templates are always up to date, and track template performance across the entire organization. All metrics on a team template reflect usage across the team; individual metrics can be found with the email_templates API endpoint. 

    :param ids: IDs of team templates to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[str]
    :param updated_at: Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type updated_at: List[str]
    :param search: Filters email templates by title or subject
    :type search: str
    :param tag_ids: Filters email templates by tags applied to the template by tag ID, not to exceed 100 IDs
    :type tag_ids: List[int]
    :param tag: Filters team templates by tags applied to the template, not to exceed 100 tags
    :type tag: List[str]
    :param include_archived_templates: Filters email templates to include archived templates or not
    :type include_archived_templates: bool
    :param sort_by: Key to sort on, must be one of: created_at, updated_at, last_used_at. Defaults to updated_at
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
