# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.broadcasts_response import BroadcastsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_broadcasts_get(client):
    """Test case for broadcasts_get

    Broadcasts
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('service_id', 'service_id_example'),
                    ('date', '_date_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/broadcasts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_broadcasts_latest_get(client):
    """Test case for broadcasts_latest_get

    Latest Broadcasts
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('service_id', 'service_id_example'),
                    ('on_air', 'on_air_example'),
                    ('next', 'next_example'),
                    ('previous', 'previous_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/broadcasts/latest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_broadcast_by_pid(client):
    """Test case for get_broadcast_by_pid

    Broadcasts by PID
    """
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/broadcasts/{pid}'.format(pid='pid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

