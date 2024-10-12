from typing import List, Dict
from aiohttp import web

from openapi_server.models.crm_activity_field import CrmActivityField
from openapi_server import util


async def v2_crm_activity_fields_json_get(request: web.Request, source=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List crm activity fields

    Fetches multiple crm activity field records. The records can be filtered, paged, and sorted according to the respective parameters. 

    :param source: Return only records with this source
    :type source: str
    :param sort_by: Key to sort on, must be one of: title, updated_at. Defaults to title
    :type sort_by: str
    :param sort_direction: Direction to sort in, must be one of: ASC, DESC. Defaults to ASC
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
