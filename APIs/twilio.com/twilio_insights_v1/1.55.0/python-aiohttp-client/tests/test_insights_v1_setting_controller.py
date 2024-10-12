# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.insights_v1_account_settings import InsightsV1AccountSettings


pytestmark = pytest.mark.asyncio

async def test_fetch_account_settings(client):
    """Test case for fetch_account_settings

    
    """
    params = [('SubaccountSid', 'subaccount_sid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Voice/Settings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_account_settings(client):
    """Test case for update_account_settings

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'advanced_features': True,
        'subaccount_sid': 'subaccount_sid_example',
        'voice_trace': True
        }
    response = await client.request(
        method='POST',
        path='/v1/Voice/Settings',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

