# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.oauth_v1_openid_discovery import OauthV1OpenidDiscovery


pytestmark = pytest.mark.asyncio

async def test_fetch_openid_discovery(client):
    """Test case for fetch_openid_discovery

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/.well-known/openid-configuration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

