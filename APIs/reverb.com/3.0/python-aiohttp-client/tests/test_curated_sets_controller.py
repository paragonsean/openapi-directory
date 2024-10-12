# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_curated_sets_slug_get(client):
    """Test case for curated_sets_slug_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/curated_sets/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

