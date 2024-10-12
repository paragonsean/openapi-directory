# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_tier_price_management_v1_remove_delete(client):
    """Test case for catalog_product_tier_price_management_v1_remove_delete

    products/{sku}/group-prices/{customerGroupId}/tiers/{qty}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/products/{sku}/group-prices/{customer_group_id}/tiers/{qty}'.format(sku='sku_example', customer_group_id='customer_group_id_example', qty=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

