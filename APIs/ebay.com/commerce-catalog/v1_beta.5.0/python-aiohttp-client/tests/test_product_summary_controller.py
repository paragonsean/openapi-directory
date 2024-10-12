# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_search_response import ProductSearchResponse


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    
    """
    params = [('aspect_filter', 'aspect_filter_example'),
                    ('category_ids', 'category_ids_example'),
                    ('fieldgroups', 'fieldgroups_example'),
                    ('gtin', 'gtin_example'),
                    ('limit', 'limit_example'),
                    ('mpn', 'mpn_example'),
                    ('offset', 'offset_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commerce/catalog/v1_beta/product_summary/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

