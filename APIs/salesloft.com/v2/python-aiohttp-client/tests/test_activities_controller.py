# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity import Activity


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_activities_json_post(client):
    """Test case for v2_activities_json_post

    Create an activity
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'action_id': 56,
        'task_id': 56
        }
    response = await client.request(
        method='POST',
        path='/v2/activities.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

