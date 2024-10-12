# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deal_item_search_response import DealItemSearchResponse


pytestmark = pytest.mark.asyncio

async def test_get_deal_items(client):
    """Test case for get_deal_items

    
    """
    params = [('category_ids', 'category_ids_example'),
                    ('commissionable', 'commissionable_example'),
                    ('delivery_country', 'delivery_country_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buy/deal/v1/deal_item',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

