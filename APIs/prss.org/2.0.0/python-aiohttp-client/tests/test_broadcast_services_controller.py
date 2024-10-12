# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.broadcast_service import BroadcastService
from openapi_server.models.episode import Episode
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_api_v2_broadcastservices_get(client):
    """Test case for api_v2_broadcastservices_get

    Gets broadcast services matching the given criteria.
    """
    params = [('pageStart', 0),
                    ('pageSize', 500),
                    ('orderById', 'order_by_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/broadcastservices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_broadcastservices_id_get(client):
    """Test case for api_v2_broadcastservices_id_get

    Returns the broadcast service matching the given ID.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/broadcastservices/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

