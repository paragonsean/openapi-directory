# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity import Activity


pytestmark = pytest.mark.asyncio

async def test_all_activities(client):
    """Test case for all_activities

    All activities for current user
    """
    params = [('start_time', '2013-10-20T19:20:30+01:00'),
                    ('end_time', '2013-10-20T19:20:30+01:00'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/activities'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destroy_activities(client):
    """Test case for destroy_activities

    All activities for current user
    """
    headers = { 
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/{username}/activities'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_activity(client):
    """Test case for get_activity

    Get activities by type for current user
    """
    params = [('start_time', '2013-10-20T19:20:30+01:00'),
                    ('end_time', '2013-10-20T19:20:30+01:00'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/activities/{type}'.format(username='username_example', type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

