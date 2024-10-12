# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.stats import Stats


pytestmark = pytest.mark.asyncio

async def test_global_live_stats(client):
    """Test case for global_live_stats

    Get global otoroshi stats
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/live',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_live_stats(client):
    """Test case for service_live_stats

    Get live feed of otoroshi stats
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/live/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

