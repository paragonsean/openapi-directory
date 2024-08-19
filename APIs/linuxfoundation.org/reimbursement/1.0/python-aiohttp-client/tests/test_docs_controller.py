# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_doc(client):
    """Test case for get_doc

    Get swagger documentation
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/api-docs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

