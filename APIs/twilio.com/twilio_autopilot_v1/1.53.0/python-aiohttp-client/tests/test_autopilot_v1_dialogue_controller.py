# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_dialogue import AutopilotV1AssistantDialogue


pytestmark = pytest.mark.asyncio

async def test_fetch_dialogue(client):
    """Test case for fetch_dialogue

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Assistants/{assistant_sid}/Dialogues/{sid}'.format(assistant_sid='assistant_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

