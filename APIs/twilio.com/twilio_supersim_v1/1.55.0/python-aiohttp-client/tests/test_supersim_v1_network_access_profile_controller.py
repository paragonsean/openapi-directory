# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_network_access_profile_response import ListNetworkAccessProfileResponse
from openapi_server.models.supersim_v1_network_access_profile import SupersimV1NetworkAccessProfile


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_network_access_profile(client):
    """Test case for create_network_access_profile

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'networks': ['networks_example'],
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/NetworkAccessProfiles',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_network_access_profile(client):
    """Test case for fetch_network_access_profile

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/NetworkAccessProfiles/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_network_access_profile(client):
    """Test case for list_network_access_profile

    
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
        path='/v1/NetworkAccessProfiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_network_access_profile(client):
    """Test case for update_network_access_profile

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/NetworkAccessProfiles/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

