from typing import List, Dict
from aiohttp import web

from openapi_server.models.users_invite_vendor_user_post_request import UsersInviteVendorUserPostRequest
from openapi_server.models.vendor_users_post_request import VendorUsersPostRequest
from openapi_server import util


async def users_invite_vendor_user_post_0(request: web.Request, data) -> web.Response:
    """Invite a VendorUser (Team member)

    

    :param data: 
    :type data: dict | bytes

    """
    data = UsersInviteVendorUserPostRequest.from_dict(data)
    return web.Response(status=200)


async def vendor_users_post_0(request: web.Request, data) -> web.Response:
    """Create or update a team member by their external_id

    the POST /vendor_users is very similar to the POST /users/invite_vendor_user but /vendor_users is intended for consumers to refresh team member data periodically, rather than just a one-off user creation.

    :param data: 
    :type data: dict | bytes

    """
    data = VendorUsersPostRequest.from_dict(data)
    return web.Response(status=200)
