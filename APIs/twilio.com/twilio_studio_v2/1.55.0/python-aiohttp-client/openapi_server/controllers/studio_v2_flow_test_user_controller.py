from typing import List, Dict
from aiohttp import web

from openapi_server.models.studio_v2_flow_test_user import StudioV2FlowTestUser
from openapi_server import util


async def fetch_test_user(request: web.Request, sid) -> web.Response:
    """fetch_test_user

    Fetch flow test users

    :param sid: Unique identifier of the flow.
    :type sid: str

    """
    return web.Response(status=200)


async def update_test_user(request: web.Request, sid, test_users) -> web.Response:
    """update_test_user

    Update flow test users

    :param sid: Unique identifier of the flow.
    :type sid: str
    :param test_users: List of test user identities that can test draft versions of the flow.
    :type test_users: List[str]

    """
    return web.Response(status=200)
