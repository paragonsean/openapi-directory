from typing import List, Dict
from aiohttp import web

from openapi_server.models.user import User
from openapi_server import util


async def v2_users_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch a user

    Fetches a user, by ID only. 

    :param id: User ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_users_id_json_put(request: web.Request, id, active=None, group_id=None, role_id=None, work_country=None) -> web.Response:
    """Update a user

    Updates a user. 

    :param id: User ID
    :type id: str
    :param active: Active status of the user&#39;s account
    :type active: bool
    :param group_id: Group assigned to the user
    :type group_id: int
    :param role_id: Role assigned to the user. Must be one of: Admin, User, or a custom role ID
    :type role_id: str
    :param work_country: The user&#39;s work country (alpha-2 code)
    :type work_country: str

    """
    return web.Response(status=200)


async def v2_users_json_get(request: web.Request, ids=None, guid=None, group_id=None, role_id=None, search=None, active=None, visible_only=None, per_page=None, page=None, include_paging_counts=None, has_crm_user=None, work_country=None, sort_by=None, sort_direction=None) -> web.Response:
    """List users

    Non Admin: Lists only your user, or all on team depending on group visibility policy Team Admin: Lists users associated with your team 

    :param ids: IDs of users to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param guid: Filters list to only include guids
    :type guid: List[str]
    :param group_id: Filters users by group_id.  An additional value of \&quot;_is_null\&quot; can be passed to filter users that are not in a group
    :type group_id: List[str]
    :param role_id: Filters users by role_id
    :type role_id: List[str]
    :param search: Space-separated list of keywords used to find case-insensitive substring matches against First Name, Last Name, or Email
    :type search: str
    :param active: Filters users based on active attribute. Defaults to not applied
    :type active: bool
    :param visible_only: Defaults to true.  When true, only shows users that are actionable based on the team&#39;s privacy settings. When false, shows all users on the team, even if you can&#39;t take action on that user. Deactivated users are also included when false. 
    :type visible_only: bool
    :param per_page: How many users to show per page in the range [1, 100]. Defaults to 25.  Results are only paginated if the page parameter is defined
    :type per_page: int
    :param page: The current page to fetch users from. Defaults to returning all users
    :type page: int
    :param include_paging_counts: Whether to include total_pages and total_count in the metadata. Defaults to false
    :type include_paging_counts: bool
    :param has_crm_user: Filters users based on if they have a crm user mapped or not.
    :type has_crm_user: bool
    :param work_country: Filters users based on assigned work_country.
    :type work_country: List[str]
    :param sort_by: Key to sort on, must be one of: id, email, name, group, role. Defaults to id
    :type sort_by: str
    :param sort_direction: Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    :type sort_direction: str

    """
    return web.Response(status=200)
