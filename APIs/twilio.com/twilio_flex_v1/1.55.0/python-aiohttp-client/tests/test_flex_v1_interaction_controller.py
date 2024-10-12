# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_interaction import FlexV1Interaction


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_interaction(client):
    """Test case for create_interaction

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'channel': None,
        'interaction_context_sid': 'interaction_context_sid_example',
        'routing': None
        }
    response = await client.request(
        method='POST',
        path='/v1/Interactions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_interaction(client):
    """Test case for fetch_interaction

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Interactions/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

