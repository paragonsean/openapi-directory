# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_listing_conditions_get(client):
    """Test case for listing_conditions_get

    List of supported product conditions
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/listing_conditions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

