# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_resources_get(client):
    """Test case for resources_get

    Fetch all verses sung for a specific category of god, person, or object
    """
    params = [('sungforcategory', 'sungforcategory_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/rv/v1/resources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

