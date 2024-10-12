# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_item_search_response import EventItemSearchResponse


pytestmark = pytest.mark.asyncio

async def test_get_event_items(client):
    """Test case for get_event_items

    
    """
    params = [('category_ids', 'category_ids_example'),
                    ('delivery_country', 'delivery_country_example'),
                    ('event_ids', 'event_ids_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buy/deal/v1/event_item',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

