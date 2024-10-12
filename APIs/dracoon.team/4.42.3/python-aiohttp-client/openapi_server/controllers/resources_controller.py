from typing import List, Dict
from aiohttp import web

from openapi_server.models.avatar import Avatar
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.notification_scope_list import NotificationScopeList
from openapi_server import util


async def request_subscription_scopes(request: web.Request, ) -> web.Response:
    """Request list of subscription scopes

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description: Retrieve a list of subscription scopes.  ### Precondition: Authenticated user.  ### Postcondition: List of scopes is returned.  ### Further Information: None.


    """
    return web.Response(status=200)


async def request_user_avatar(request: web.Request, uuid, user_id) -> web.Response:
    """Request user avatar

    ### Description: Get user avatar.  ### Precondition: Valid user ID and avatar UUID  ### Postcondition: Avatar is returned.  ### Further Information: None.

    :param uuid: UUID of the avatar
    :type uuid: str
    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)
