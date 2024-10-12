# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_v1_auth_token_promotion import AccountsV1AuthTokenPromotion


pytestmark = pytest.mark.asyncio

async def test_update_auth_token_promotion(client):
    """Test case for update_auth_token_promotion

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/AuthTokens/Promote',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

