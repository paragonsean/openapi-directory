from typing import List, Dict
from aiohttp import web

from openapi_server.models.email_template import EmailTemplate
from openapi_server import util


async def v2_email_templates_id_json_get(request: web.Request, id, include_signature=None) -> web.Response:
    """Fetch an email template

    Fetches an email template, by ID only. 

    :param id: EmailTemplate ID
    :type id: str
    :param include_signature: Optionally will return the templates with the current user&#39;s email signature
    :type include_signature: bool

    """
    return web.Response(status=200)


async def v2_email_templates_json_get(request: web.Request, ids=None, updated_at=None, linked_to_team_template=None, search=None, tag_ids=None, tag=None, filter_by_owner=None, group_id=None, include_cadence_templates=None, include_archived_templates=None, cadence_id=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List email templates

    Fetches multiple email template records. The records can be filtered, paged, and sorted according to the respective parameters. 

    :param ids: IDs of email templates to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param updated_at: Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type updated_at: List[str]
    :param linked_to_team_template: Filters email templates by whether they are linked to a team template or not
    :type linked_to_team_template: bool
    :param search: Filters email templates by title or subject
    :type search: str
    :param tag_ids: Filters email templates by tags applied to the template by tag ID, not to exceed 100 IDs
    :type tag_ids: List[int]
    :param tag: Filters email templates by tags applied to the template, not to exceed 100 tags
    :type tag: List[str]
    :param filter_by_owner: Filters email templates by current authenticated user
    :type filter_by_owner: bool
    :param group_id: Filters email templates by groups applied to the template by group ID. Not to exceed 500 IDs. Returns templates that are assigned to any of the group ids.
    :type group_id: List[int]
    :param include_cadence_templates: Filters email templates based on whether or not the template has been used on a cadence
    :type include_cadence_templates: bool
    :param include_archived_templates: Filters email templates to include archived templates or not
    :type include_archived_templates: bool
    :param cadence_id: Filters email templates to those belonging to the cadence. Not to exceed 100 IDs. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type cadence_id: List[int]
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
