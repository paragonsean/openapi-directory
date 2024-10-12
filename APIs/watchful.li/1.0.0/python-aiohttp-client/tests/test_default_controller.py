# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_packages_post(client):
    """Test case for packages_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/v1/packages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

