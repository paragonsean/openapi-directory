from typing import List, Dict
from aiohttp import web

from openapi_server.models.crm_user import CrmUser
from openapi_server import util


async def v2_crm_users_json_get(request: web.Request, ids=None, crm_id=None, user_id=None, user_guid=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None, sort_by=None, sort_direction=None) -> web.Response:
    """List crm users

    Crm Users 

    :param ids: IDs of crm users to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param crm_id: Filters crm users by crm_ids
    :type crm_id: List[str]
    :param user_id: Filters crm users by user_ids
    :type user_id: List[int]
    :param user_guid: Filters crm users by user guids
    :type user_guid: List[str]
    :param per_page: How many records to show per page in the range [1, 100]. Defaults to 25
    :type per_page: int
    :param page: The current page to fetch results from. Defaults to 1
    :type page: int
    :param include_paging_counts: Whether to include total_pages and total_count in the metadata. Defaults to false
    :type include_paging_counts: bool
    :param limit_paging_counts: Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    :type limit_paging_counts: bool
    :param sort_by: Key to sort on, must be one of: id, updated_at. Defaults to id
    :type sort_by: str
    :param sort_direction: Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    :type sort_direction: str

    """
    return web.Response(status=200)
