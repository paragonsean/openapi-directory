# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_all_collections(client):
    """Test case for get_all_collections

    Get all collections
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('page', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/collections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

