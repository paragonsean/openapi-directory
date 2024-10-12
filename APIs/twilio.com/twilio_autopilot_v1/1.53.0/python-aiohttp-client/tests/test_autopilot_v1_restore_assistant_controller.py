# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autopilot_v1_restore_assistant import AutopilotV1RestoreAssistant


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_restore_assistant(client):
    """Test case for update_restore_assistant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'assistant': 'assistant_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Assistants/Restore',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

