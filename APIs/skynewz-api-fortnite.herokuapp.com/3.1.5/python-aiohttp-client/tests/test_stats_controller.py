# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_get_default_response import CheckGetDefaultResponse
from openapi_server.models.stats_id_plateform_id_get200_response import StatsIdPlateformIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_stats_id_plateform_id_get(client):
    """Test case for stats_id_plateform_id_get

    Get user's stats by user id
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/stats/id/{plateform}/{id}'.format(plateform='plateform_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stats_plateform_username_get(client):
    """Test case for stats_plateform_username_get

    Get user's stats by username
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/stats/{plateform}/{username}'.format(plateform='plateform_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

