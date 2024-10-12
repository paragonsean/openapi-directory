from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.multi_exchange_rate_list_vo import MultiExchangeRateListVO
from openapi_server.models.multi_exchange_rate_persist_list_vo import MultiExchangeRatePersistListVO
from openapi_server import util


async def get_exchange_rate_list(request: web.Request, workgroup_id) -> web.Response:
    """Get Exchange Rate List

    Get Exchange Rate List

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def post_exchange_rate(request: web.Request, workgroup_id, body=None) -> web.Response:
    """Create Exchange Rates

    Create Exchange Rates

    :param workgroup_id: 
    :type workgroup_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MultiExchangeRatePersistListVO.from_dict(body)
    return web.Response(status=200)
