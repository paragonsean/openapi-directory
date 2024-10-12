from typing import List, Dict
from aiohttp import web

from openapi_server.models.broadcasts_response import BroadcastsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def broadcasts_get(request: web.Request, x_api_key, offset=None, limit=None, service_id=None, _date=None, sort=None) -> web.Response:
    """Broadcasts

    All broadcasts 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int
    :param service_id: Filter by Service ID. E.g. bbc_radio_fourfm
    :type service_id: str
    :param _date: Filter by date. E.g. 2016-06-17
    :type _date: str
    :param sort: Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order
    :type sort: str

    """
    return web.Response(status=200)


async def broadcasts_latest_get(request: web.Request, x_api_key, offset=None, limit=None, service_id=None, on_air=None, next=None, previous=None, sort=None) -> web.Response:
    """Latest Broadcasts

    Broadcasts for the current day 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int
    :param service_id: Filter by Service ID. E.g. bbc_radio_fourfm
    :type service_id: str
    :param on_air: Filter what is on air. E.g. &#39;now&#39; returns current programme being broadcasted.
    :type on_air: str
    :param next: Filter what will be on air next in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the next four hurs
    :type next: str
    :param previous: Filter what was on air previously in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the previous four hurs
    :type previous: str
    :param sort: Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order
    :type sort: str

    """
    return web.Response(status=200)


async def get_broadcast_by_pid(request: web.Request, x_api_key, pid) -> web.Response:
    """Broadcasts by PID

    Find broadcast by PID 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param pid: pid
    :type pid: str

    """
    return web.Response(status=200)
