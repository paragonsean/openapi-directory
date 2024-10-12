# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.best_selling_product_response import BestSellingProductResponse


pytestmark = pytest.mark.asyncio

async def test_get_merchandised_products(client):
    """Test case for get_merchandised_products

    
    """
    params = [('aspect_filter', 'aspect_filter_example'),
                    ('category_id', 'category_id_example'),
                    ('limit', 'limit_example'),
                    ('metric_name', 'metric_name_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buy/marketing/v1_beta/merchandised_product',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

