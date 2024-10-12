# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_inventory_stock_registry_v1_update_stock_item_by_sku_put_request import CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_inventory_stock_registry_v1_update_stock_item_by_sku_put(client):
    """Test case for catalog_inventory_stock_registry_v1_update_stock_item_by_sku_put

    products/{productSku}/stockItems/{itemId}
    """
    body = openapi_server.CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/products/{product_sku}/stockItems/{item_id}'.format(product_sku='product_sku_example', item_id='item_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

