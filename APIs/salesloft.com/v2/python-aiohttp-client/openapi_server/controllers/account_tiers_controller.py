from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_tier import AccountTier
from openapi_server import util


async def v2_account_tiers_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch an account tier

    Fetches an account tier, by ID only. 

    :param id: Account Tier ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_account_tiers_json_get(request: web.Request, ids=None, name=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List Account Tiers

    Fetches multiple account tier records. The records can be filtered, paged, and sorted according to the respective parameters. 

    :param ids: IDs of Account Tiers to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param name: Filters Account Tiers by name. Multiple names can be applied
    :type name: List[str]
    :param sort_by: Key to sort on, must be one of: created_at, updated_at, order. Defaults to updated_at
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
