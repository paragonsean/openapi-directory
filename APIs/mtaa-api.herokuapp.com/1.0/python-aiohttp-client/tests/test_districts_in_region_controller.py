# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_districts_in_a_region(client):
    """Test case for districts_in_a_region

    Returns all districts in region
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/{country}/{region}'.format(country='country_example', region='region_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

