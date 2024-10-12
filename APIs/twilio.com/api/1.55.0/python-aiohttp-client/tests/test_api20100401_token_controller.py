# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_token import ApiV2010AccountToken


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_token(client):
    """Test case for create_token

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'ttl': 56
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Tokens.json'.format(account_sid='account_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

