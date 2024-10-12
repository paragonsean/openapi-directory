# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.previous_asset_purchases import PreviousAssetPurchases


pytestmark = pytest.mark.asyncio

async def test_v3_purchased_assets_get(client):
    """Test case for v3_purchased_assets_get

    Get Previously Purchased Images and Video
    """
    params = [('date_to', '2013-10-20T19:20:30+01:00'),
                    ('page', 1),
                    ('page_size', 75),
                    ('date_from', '2013-10-20T19:20:30+01:00'),
                    ('company_purchases', False)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/purchased-assets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

