from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_base_price_storage_v1_update_post_request import CatalogBasePriceStorageV1UpdatePostRequest
from openapi_server.models.catalog_data_price_update_result_interface import CatalogDataPriceUpdateResultInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_base_price_storage_v1_update_post(request: web.Request, body=None) -> web.Response:
    """products/base-prices

    Add or update product prices. Input item should correspond \\Magento\\Catalog\\Api\\Data\\CostInterface. If any items will have invalid price, store id or sku, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

    :param body: 
    :type body: dict | bytes

    """
    body = CatalogBasePriceStorageV1UpdatePostRequest.from_dict(body)
    return web.Response(status=200)
