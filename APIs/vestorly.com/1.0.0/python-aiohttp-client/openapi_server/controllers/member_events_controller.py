from typing import List, Dict
from aiohttp import web

from openapi_server.models.member_events import MemberEvents
from openapi_server import util


async def find_member_events(request: web.Request, vestorly_auth, access_token=None) -> web.Response:
    """find_member_events

    Returns all MemberEvents

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)
