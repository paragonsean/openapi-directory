# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_delivery_usage_response import ListDeliveryUsageResponse


pytestmark = pytest.mark.asyncio

async def test_list_delivery_usage(client):
    """Test case for list_delivery_usage

    List Usage
    """
    params = [('page', 1),
                    ('limit', 100),
                    ('asset_id', 'asset_id_example'),
                    ('live_stream_id', 'live_stream_id_example'),
                    ('timeframe[]', ['timeframe_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/delivery-usage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

