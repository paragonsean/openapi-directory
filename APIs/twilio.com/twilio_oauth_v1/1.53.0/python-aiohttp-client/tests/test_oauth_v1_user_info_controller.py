# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.oauth_v1_user_info import OauthV1UserInfo


pytestmark = pytest.mark.asyncio

async def test_fetch_user_info(client):
    """Test case for fetch_user_info

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/userinfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

