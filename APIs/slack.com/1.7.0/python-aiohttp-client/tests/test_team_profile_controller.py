# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.team_profile_get_error_schema import TeamProfileGetErrorSchema
from openapi_server.models.team_profile_get_success_schema import TeamProfileGetSuccessSchema


pytestmark = pytest.mark.asyncio

async def test_team_profile_get(client):
    """Test case for team_profile_get

    
    """
    params = [('token', 'token_example'),
                    ('visibility', 'visibility_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/team.profile.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

