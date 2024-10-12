# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.insights_v1_call import InsightsV1Call


pytestmark = pytest.mark.asyncio

async def test_fetch_call(client):
    """Test case for fetch_call

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Voice/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

