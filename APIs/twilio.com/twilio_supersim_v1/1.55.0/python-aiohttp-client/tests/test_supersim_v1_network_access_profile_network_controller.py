# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_network_access_profile_network_response import ListNetworkAccessProfileNetworkResponse
from openapi_server.models.supersim_v1_network_access_profile_network_access_profile_network import SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_network_access_profile_network(client):
    """Test case for create_network_access_profile_network

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'network': 'network_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks'.format(network_access_profile_sid='network_access_profile_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_access_profile_network(client):
    """Test case for delete_network_access_profile_network

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}'.format(network_access_profile_sid='network_access_profile_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_network_access_profile_network(client):
    """Test case for fetch_network_access_profile_network

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}'.format(network_access_profile_sid='network_access_profile_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_network_access_profile_network(client):
    """Test case for list_network_access_profile_network

    
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
        path='/v1/NetworkAccessProfiles/{network_access_profile_sid}/Networks'.format(network_access_profile_sid='network_access_profile_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

