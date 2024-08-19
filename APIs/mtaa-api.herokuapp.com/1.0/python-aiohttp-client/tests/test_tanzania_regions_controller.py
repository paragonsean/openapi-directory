# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_tanzania_regions(client):
    """Test case for tanzania_regions

    Returns all regions present in Tanzania
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/{country}'.format(country='country_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

