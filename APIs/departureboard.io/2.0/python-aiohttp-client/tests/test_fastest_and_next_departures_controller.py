# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_fastest_departures_by_crs(client):
    """Test case for get_fastest_departures_by_crs

    getFastestDeparturesByCRS is used to get the fastest next service running between two stations. Multiple destinations can be specified. This will typically return a single train service, but will also return a replacement bus or ferry service if in place.
    """
    params = [('apiKey', 'api_key_example'),
                    ('filterList', 'filter_list_example'),
                    ('timeOffset', 0),
                    ('timeWindow', 120),
                    ('serviceDetails', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/getFastestDeparturesByCRS/{crs}'.format(crs='crs_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_next_departures_by_crs(client):
    """Test case for get_next_departures_by_crs

    getNextDeparturesByCRS is used to get the next service running between two stations. Multiple destinations can be specified. This will typically return a single train service, but will also return a replacement bus or ferry service if in place. This will return the next departures for each of the filterList stations specified. It may not return the fastest next service. To get the fastest next service use the getFastestDeparturesByCRS endpoint.
    """
    params = [('apiKey', 'api_key_example'),
                    ('filterList', 'filter_list_example'),
                    ('timeOffset', 0),
                    ('timeWindow', 120),
                    ('serviceDetails', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/getNextDeparturesByCRS/{crs}'.format(crs='crs_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

