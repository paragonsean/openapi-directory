# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_gsi_besthour_0(client):
    """Test case for gsi_besthour_0

    Get best hour (with most regional green energy) in a given timeframe.
    """
    params = [('zip', 'zip_example'),
                    ('key', 'key_example'),
                    ('timeframe', 56),
                    ('hours', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/gsi/bestHour',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

