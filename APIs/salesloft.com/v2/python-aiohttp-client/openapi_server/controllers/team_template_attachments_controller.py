from typing import List, Dict
from aiohttp import web

from openapi_server.models.team_template_attachment import TeamTemplateAttachment
from openapi_server import util


async def v2_team_template_attachments_json_get(request: web.Request, ids=None, team_template_id=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List team template attachments

    Fetches multiple team template attachment records. The records can be filtered and paged according to the respective parameters. 

    :param ids: IDs of team template attachments to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param team_template_id: Filters template attachments by team template IDs
    :type team_template_id: List[int]
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
