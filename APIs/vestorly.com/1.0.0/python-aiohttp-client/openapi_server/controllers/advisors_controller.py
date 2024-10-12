from typing import List, Dict
from aiohttp import web

from openapi_server.models.advisor import Advisor
from openapi_server import util


async def find_advisor_by_id(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """find_advisor_by_id

    Returns a single advisor given their ID

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: Advisor Id to fetch
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)
