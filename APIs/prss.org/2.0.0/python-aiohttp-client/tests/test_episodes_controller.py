# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.episode import Episode
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_api_v2_episodes_get(client):
    """Test case for api_v2_episodes_get

    Gets episodes matching the given criteria.
    """
    params = [('id', 56),
                    ('beginAirDateAfter', '2013-10-20T19:20:30+01:00'),
                    ('endAirDateBefore', '2013-10-20T19:20:30+01:00'),
                    ('programId', 56),
                    ('pageStart', 0),
                    ('pageSize', 500),
                    ('orderById', 'order_by_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/episodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_episodes_id_get(client):
    """Test case for api_v2_episodes_id_get

    Returns the episode matching the given ID.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/episodes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

