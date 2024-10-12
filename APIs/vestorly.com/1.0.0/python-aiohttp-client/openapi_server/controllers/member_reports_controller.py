from typing import List, Dict
from aiohttp import web

from openapi_server.models.member_reports import MemberReports
from openapi_server import util


async def find_member_reports(request: web.Request, vestorly_auth, access_token=None) -> web.Response:
    """find_member_reports

    Returns all member reports

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)
