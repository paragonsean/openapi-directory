# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.team_teamname_get200_response import TeamTeamnameGet200Response


pytestmark = pytest.mark.asyncio

async def test_team_teamname_get(client):
    """Test case for team_teamname_get

    Get a Team
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/team/{teamname}'.format(teamname='teamname_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

