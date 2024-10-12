from typing import List, Dict
from aiohttp import web

from openapi_server.models.order_detail import OrderDetail
from openapi_server import util


async def v3_orders_id_get(request: web.Request, id, accept_language=None) -> web.Response:
    """Get order metadata

    This endpoint returns detailed order metadata for a specified order. Use of this endpoint requires configuration changes to your API key.   You&#39;ll need an API key and access token to use this resource.

    :param id: An order id.
    :type id: int
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str

    """
    return web.Response(status=200)
