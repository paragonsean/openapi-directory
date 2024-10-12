# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_inventory_data_stock_status_interface import CatalogInventoryDataStockStatusInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_inventory_stock_registry_v1_get_stock_status_by_sku_get(client):
    """Test case for catalog_inventory_stock_registry_v1_get_stock_status_by_sku_get

    stockStatuses/{productSku}
    """
    params = [('scopeId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/stockStatuses/{product_sku}'.format(product_sku='product_sku_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

