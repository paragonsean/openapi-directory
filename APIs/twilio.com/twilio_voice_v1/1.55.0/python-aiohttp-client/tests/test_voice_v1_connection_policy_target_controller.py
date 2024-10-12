# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_connection_policy_target_response import ListConnectionPolicyTargetResponse
from openapi_server.models.voice_v1_connection_policy_connection_policy_target import VoiceV1ConnectionPolicyConnectionPolicyTarget


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_connection_policy_target(client):
    """Test case for create_connection_policy_target

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'enabled': True,
        'friendly_name': 'friendly_name_example',
        'priority': 56,
        'target': 'target_example',
        'weight': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/ConnectionPolicies/{connection_policy_sid}/Targets'.format(connection_policy_sid='connection_policy_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_connection_policy_target(client):
    """Test case for delete_connection_policy_target

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}'.format(connection_policy_sid='connection_policy_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_connection_policy_target(client):
    """Test case for fetch_connection_policy_target

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}'.format(connection_policy_sid='connection_policy_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_connection_policy_target(client):
    """Test case for list_connection_policy_target

    
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
        path='/v1/ConnectionPolicies/{connection_policy_sid}/Targets'.format(connection_policy_sid='connection_policy_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_connection_policy_target(client):
    """Test case for update_connection_policy_target

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'enabled': True,
        'friendly_name': 'friendly_name_example',
        'priority': 56,
        'target': 'target_example',
        'weight': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}'.format(connection_policy_sid='connection_policy_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

