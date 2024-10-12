# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.team import Team


pytestmark = pytest.mark.asyncio

async def test_v2_team_json_get(client):
    """Test case for v2_team_json_get

    Fetch current team
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/team.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

