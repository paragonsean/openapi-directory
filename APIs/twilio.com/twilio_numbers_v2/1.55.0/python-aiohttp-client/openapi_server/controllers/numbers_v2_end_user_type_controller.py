from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_end_user_type_response import ListEndUserTypeResponse
from openapi_server.models.numbers_v2_regulatory_compliance_end_user_type import NumbersV2RegulatoryComplianceEndUserType
from openapi_server import util


async def fetch_end_user_type(request: web.Request, sid) -> web.Response:
    """fetch_end_user_type

    Fetch a specific End-User Type Instance.

    :param sid: The unique string that identifies the End-User Type resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_end_user_type(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_end_user_type

    Retrieve a list of all End-User Types.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
