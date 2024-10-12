from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_tier_price_management_v1_remove_delete(request: web.Request, sku, customer_group_id, qty) -> web.Response:
    """products/{sku}/group-prices/{customerGroupId}/tiers/{qty}

    Remove tier price from product

    :param sku: 
    :type sku: str
    :param customer_group_id: &#39;all&#39; can be used to specify &#39;ALL GROUPS&#39;
    :type customer_group_id: str
    :param qty: 
    :type qty: 

    """
    return web.Response(status=200)
