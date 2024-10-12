from typing import List, Dict
from aiohttp import web

from openapi_server.models.organizer import Organizer
from openapi_server import util


async def get_all_organisers(request: web.Request, authorization, account_key) -> web.Response:
    """DEPRECATED: Get Organizers

    DEPRECATED: Please use the Admin API call &#39;Get all users&#39; instead. For details see https://goto-developer.logmein.com/get-all-users.

    :param authorization: Access token
    :type authorization: str
    :param account_key: The key of the multi-user account
    :type account_key: int

    """
    return web.Response(status=200)
