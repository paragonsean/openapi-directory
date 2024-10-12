# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_balance import ApiV2010AccountBalance


pytestmark = pytest.mark.asyncio

async def test_fetch_balance(client):
    """Test case for fetch_balance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Balance.json'.format(account_sid='account_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

