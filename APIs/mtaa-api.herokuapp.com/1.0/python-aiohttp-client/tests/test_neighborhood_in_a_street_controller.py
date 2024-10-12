# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_neighborhood_in_a_street(client):
    """Test case for neighborhood_in_a_street

    Returns all neighborhood in a street
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/{country}/{region}/{district}/{ward}/{street}'.format(country='country_example', region='region_example', district='district_example', ward='ward_example', street='street_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

