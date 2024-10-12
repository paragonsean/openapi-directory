from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_inventory_data_stock_item_collection_interface import CatalogInventoryDataStockItemCollectionInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_inventory_stock_registry_v1_get_low_stock_items_get(request: web.Request, scope_id, qty, current_page=None, page_size=None) -> web.Response:
    """stockItems/lowStock/

    Retrieves a list of SKU&#39;s with low inventory qty

    :param scope_id: 
    :type scope_id: int
    :param qty: 
    :type qty: 
    :param current_page: 
    :type current_page: int
    :param page_size: 
    :type page_size: int

    """
    return web.Response(status=200)
