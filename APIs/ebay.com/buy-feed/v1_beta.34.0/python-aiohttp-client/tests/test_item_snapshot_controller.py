# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.item_snapshot_response import ItemSnapshotResponse


pytestmark = pytest.mark.asyncio

async def test_get_item_snapshot_feed(client):
    """Test case for get_item_snapshot_feed

    
    """
    params = [('category_id', 'category_id_example'),
                    ('snapshot_date', 'snapshot_date_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'range': 'range_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buy/feed/v1_beta/item_snapshot',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

