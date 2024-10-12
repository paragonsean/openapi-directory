from typing import List, Dict
from aiohttp import web

from openapi_server.models.frontline_v1_user import FrontlineV1User
from openapi_server.models.user_enum_state_type import UserEnumStateType
from openapi_server import util


async def fetch_user(request: web.Request, sid) -> web.Response:
    """fetch_user

    Fetch a frontline user

    :param sid: The SID of the User resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def update_user(request: web.Request, sid, avatar=None, friendly_name=None, is_available=None, state=None) -> web.Response:
    """update_user

    Update an existing frontline user

    :param sid: The SID of the User resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to update.
    :type sid: str
    :param avatar: The avatar URL which will be shown in Frontline application.
    :type avatar: str
    :param friendly_name: The string that you assigned to describe the User.
    :type friendly_name: str
    :param is_available: Whether the User is available for new conversations. Set to &#x60;false&#x60; to prevent User from receiving new inbound conversations if you are using [Pool Routing](https://www.twilio.com/docs/frontline/handle-incoming-conversations#3-pool-routing).
    :type is_available: bool
    :param state: 
    :type state: str

    """
    return web.Response(status=200)
