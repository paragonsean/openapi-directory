from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_list import UserList
from openapi_server import util


async def user_profile_get(request: web.Request, roles=None, tags=None, current_user_only=None, company_idfk=None) -> web.Response:
    """Get Collection of Users who have roles in the current Avaza account.

    Admin and Invoice Managers can see all. Other users are limited to seeing their own profile.

    :param roles: Optional list of comma separated role codes to filter users by (e.g. \&quot;TimesheetUser,Admin\&quot;)
    :type roles: str
    :param tags: 
    :type tags: str
    :param current_user_only: Optional boolean (true/false) to filter to only show current authenticated user (always true for non Admin/InvoiceManager users)
    :type current_user_only: bool
    :param company_idfk: Optionally filter by Company ID
    :type company_idfk: int

    """
    return web.Response(status=200)
