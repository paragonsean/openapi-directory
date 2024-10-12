# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_wireless_rate_plan_response import ListWirelessRatePlanResponse
from openapi_server.models.preview_wireless_rate_plan import PreviewWirelessRatePlan


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_wireless_rate_plan(client):
    """Test case for create_wireless_rate_plan

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'commands_enabled': True,
        'data_enabled': True,
        'data_limit': 56,
        'data_metering': 'data_metering_example',
        'friendly_name': 'friendly_name_example',
        'international_roaming': ['international_roaming_example'],
        'messaging_enabled': True,
        'national_roaming_enabled': True,
        'unique_name': 'unique_name_example',
        'voice_enabled': True
        }
    response = await client.request(
        method='POST',
        path='/wireless/RatePlans',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_wireless_rate_plan(client):
    """Test case for delete_wireless_rate_plan

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/wireless/RatePlans/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_wireless_rate_plan(client):
    """Test case for fetch_wireless_rate_plan

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/wireless/RatePlans/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_wireless_rate_plan(client):
    """Test case for list_wireless_rate_plan

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/wireless/RatePlans',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_wireless_rate_plan(client):
    """Test case for update_wireless_rate_plan

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'friendly_name': 'friendly_name_example',
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/wireless/RatePlans/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

