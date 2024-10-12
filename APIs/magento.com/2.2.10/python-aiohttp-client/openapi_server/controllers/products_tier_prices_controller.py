from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_price_update_result_interface import CatalogDataPriceUpdateResultInterface
from openapi_server.models.catalog_tier_price_storage_v1_replace_put_request import CatalogTierPriceStorageV1ReplacePutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_tier_price_storage_v1_replace_put(request: web.Request, body=None) -> web.Response:
    """products/tier-prices

    Remove existing tier prices and replace them with the new ones. If any items will have invalid price, price type, website id, sku, customer group or quantity, they will be marked as failed and excluded from replace list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

    :param body: 
    :type body: dict | bytes

    """
    body = CatalogTierPriceStorageV1ReplacePutRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_tier_price_storage_v1_update_post(request: web.Request, body=None) -> web.Response:
    """products/tier-prices

    Add or update product prices. If any items will have invalid price, price type, website id, sku, customer group or quantity, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

    :param body: 
    :type body: dict | bytes

    """
    body = CatalogTierPriceStorageV1ReplacePutRequest.from_dict(body)
    return web.Response(status=200)
