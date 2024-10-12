# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_reports_get(client):
    """Test case for reports_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/reports',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

