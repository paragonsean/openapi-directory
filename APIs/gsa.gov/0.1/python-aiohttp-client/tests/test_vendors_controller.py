# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_list_vendors_get(client):
    """Test case for list_vendors_get

    This endpoint returns a list of vendors filtered by a NAICS code
    """
    params = [('naics', 'naics_example'),
                    ('setasides', ['setasides_example']),
                    ('vehicle', 'vehicle_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/vendors/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

