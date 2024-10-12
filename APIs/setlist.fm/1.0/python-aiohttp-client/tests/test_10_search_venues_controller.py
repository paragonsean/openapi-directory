# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_venues import JsonVenues


pytestmark = pytest.mark.asyncio

async def test_resource10_search_venues_get_venues_get(client):
    """Test case for resource10_search_venues_get_venues_get

    Search for venues.
    """
    params = [('cityId', 'city_id_example'),
                    ('cityName', 'city_name_example'),
                    ('country', 'country_example'),
                    ('name', 'name_example'),
                    ('p', 1),
                    ('state', 'state_example'),
                    ('stateCode', 'state_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/1.0/search/venues',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

