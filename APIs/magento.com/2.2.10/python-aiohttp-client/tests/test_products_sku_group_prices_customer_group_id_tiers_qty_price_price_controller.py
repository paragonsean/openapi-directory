# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_tier_price_management_v1_add_post(client):
    """Test case for catalog_product_tier_price_management_v1_add_post

    products/{sku}/group-prices/{customerGroupId}/tiers/{qty}/price/{price}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/{sku}/group-prices/{customer_group_id}/tiers/{qty}/price/{price}'.format(sku='sku_example', customer_group_id='customer_group_id_example', price=3.4, qty=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

