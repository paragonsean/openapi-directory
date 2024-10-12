from typing import List, Dict
from aiohttp import web

from openapi_server.models.available_vendors_filter import AvailableVendorsFilter
from openapi_server.models.user_list import UserList
from openapi_server import util


async def get_available_vendors(request: web.Request, _with=None, body=None) -> web.Response:
    """Get a list of vendors available for the criteria given

    Get a list of vendors available for the criteria given

    :param _with: Include detailed information. Possible values &#39;user&#39;. Requesting user info enrichment takes much longer.
    :type _with: List[str]
    :param body: 
    :type body: dict | bytes

    """
    body = AvailableVendorsFilter.from_dict(body)
    return web.Response(status=200)
