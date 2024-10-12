# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.oauth_v1_certs import OauthV1Certs


pytestmark = pytest.mark.asyncio

async def test_fetch_certs(client):
    """Test case for fetch_certs

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/certs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

