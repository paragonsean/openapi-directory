from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_inventory_data_stock_status_interface import CatalogInventoryDataStockStatusInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_inventory_stock_registry_v1_get_stock_status_by_sku_get(request: web.Request, product_sku, scope_id=None) -> web.Response:
    """stockStatuses/{productSku}

    

    :param product_sku: 
    :type product_sku: str
    :param scope_id: 
    :type scope_id: int

    """
    return web.Response(status=200)
