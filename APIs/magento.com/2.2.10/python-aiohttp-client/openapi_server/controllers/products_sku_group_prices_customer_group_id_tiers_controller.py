from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_tier_price_interface import CatalogDataProductTierPriceInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_tier_price_management_v1_get_list_get(request: web.Request, sku, customer_group_id) -> web.Response:
    """products/{sku}/group-prices/{customerGroupId}/tiers

    Get tier price of product

    :param sku: 
    :type sku: str
    :param customer_group_id: &#39;all&#39; can be used to specify &#39;ALL GROUPS&#39;
    :type customer_group_id: str

    """
    return web.Response(status=200)
