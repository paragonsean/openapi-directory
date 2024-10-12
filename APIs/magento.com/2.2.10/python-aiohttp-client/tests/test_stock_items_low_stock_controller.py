# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_inventory_data_stock_item_collection_interface import CatalogInventoryDataStockItemCollectionInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_inventory_stock_registry_v1_get_low_stock_items_get(client):
    """Test case for catalog_inventory_stock_registry_v1_get_low_stock_items_get

    stockItems/lowStock/
    """
    params = [('scopeId', 56),
                    ('qty', 3.4),
                    ('currentPage', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/stockItems/lowStock/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

