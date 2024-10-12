# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.messaging_v1_deactivation import MessagingV1Deactivation


pytestmark = pytest.mark.asyncio

async def test_fetch_deactivation(client):
    """Test case for fetch_deactivation

    
    """
    params = [('Date', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Deactivations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

