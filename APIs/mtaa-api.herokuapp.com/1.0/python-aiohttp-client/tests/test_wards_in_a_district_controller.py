# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_wards_in_a_district(client):
    """Test case for wards_in_a_district

    Returns all wards in a district
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/{country}/{region}/{district}'.format(country='country_example', region='region_example', district='district_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

