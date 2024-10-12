# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_insights_user_roles import FlexV1InsightsUserRoles


pytestmark = pytest.mark.asyncio

async def test_fetch_insights_user_roles(client):
    """Test case for fetch_insights_user_roles

    
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Insights/UserRoles',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

