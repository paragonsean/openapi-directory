from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_policies_response import ListPoliciesResponse
from openapi_server.models.trusthub_v1_policies import TrusthubV1Policies
from openapi_server import util


async def fetch_policies(request: web.Request, sid) -> web.Response:
    """fetch_policies

    Fetch specific Policy Instance.

    :param sid: The unique string that identifies the Policy resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_policies(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_policies

    Retrieve a list of all Policys.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
