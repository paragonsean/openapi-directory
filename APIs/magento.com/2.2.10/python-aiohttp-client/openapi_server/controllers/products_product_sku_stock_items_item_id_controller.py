from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_inventory_stock_registry_v1_update_stock_item_by_sku_put_request import CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_inventory_stock_registry_v1_update_stock_item_by_sku_put(request: web.Request, product_sku, item_id, body=None) -> web.Response:
    """products/{productSku}/stockItems/{itemId}

    

    :param product_sku: 
    :type product_sku: str
    :param item_id: 
    :type item_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest.from_dict(body)
    return web.Response(status=200)
