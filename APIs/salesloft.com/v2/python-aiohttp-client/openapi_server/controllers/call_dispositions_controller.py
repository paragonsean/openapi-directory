from typing import List, Dict
from aiohttp import web

from openapi_server.models.call_disposition import CallDisposition
from openapi_server import util


async def v2_call_dispositions_json_get(request: web.Request, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List call dispositions

    Fetches multiple call disposition records. The records can be sorted according to the respective parameters. Call dispositions must be configured in application. This will change in the future, but please contact us if you have a pressing use case. 

    :param sort_by: Key to sort on, must be one of: name, updated_at. Defaults to name
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
