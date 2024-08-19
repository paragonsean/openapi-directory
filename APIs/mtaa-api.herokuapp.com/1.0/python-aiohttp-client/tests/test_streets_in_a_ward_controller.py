# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_streets_in_a_ward(client):
    """Test case for streets_in_a_ward

    Returns all streets in a ward
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/{country}/{region}/{district}/{ward}'.format(country='country_example', region='region_example', district='district_example', ward='ward_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

