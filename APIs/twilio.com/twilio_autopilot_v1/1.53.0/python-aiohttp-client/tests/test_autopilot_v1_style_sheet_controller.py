# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_style_sheet import AutopilotV1AssistantStyleSheet


pytestmark = pytest.mark.asyncio

async def test_fetch_style_sheet(client):
    """Test case for fetch_style_sheet

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Assistants/{assistant_sid}/StyleSheet'.format(assistant_sid='assistant_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_style_sheet(client):
    """Test case for update_style_sheet

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'style_sheet': None
        }
    response = await client.request(
        method='POST',
        path='/v1/Assistants/{assistant_sid}/StyleSheet'.format(assistant_sid='assistant_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

