# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_fleet_response import ListFleetResponse
from openapi_server.models.supersim_v1_fleet import SupersimV1Fleet


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_fleet(client):
    """Test case for create_fleet

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'data_enabled': True,
        'data_limit': 56,
        'ip_commands_method': 'ip_commands_method_example',
        'ip_commands_url': 'ip_commands_url_example',
        'network_access_profile': 'network_access_profile_example',
        'sms_commands_enabled': True,
        'sms_commands_method': 'sms_commands_method_example',
        'sms_commands_url': 'sms_commands_url_example',
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Fleets',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_fleet(client):
    """Test case for fetch_fleet

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Fleets/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_fleet(client):
    """Test case for list_fleet

    
    """
    params = [('NetworkAccessProfile', 'network_access_profile_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Fleets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_fleet(client):
    """Test case for update_fleet

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'data_limit': 56,
        'ip_commands_method': 'ip_commands_method_example',
        'ip_commands_url': 'ip_commands_url_example',
        'network_access_profile': 'network_access_profile_example',
        'sms_commands_method': 'sms_commands_method_example',
        'sms_commands_url': 'sms_commands_url_example',
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Fleets/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

