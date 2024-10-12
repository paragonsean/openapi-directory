# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.api_key_collection import ApiKeyCollection
from openapi_server.models.blockchain_member import BlockchainMember
from openapi_server.models.blockchain_member_collection import BlockchainMemberCollection
from openapi_server.models.blockchain_member_update import BlockchainMemberUpdate
from openapi_server.models.consortium_member_collection import ConsortiumMemberCollection


pytestmark = pytest.mark.asyncio

async def test_blockchain_members_create(client):
    """Test case for blockchain_members_create

    
    """
    blockchain_member = {"sku":{"tier":"tier","name":"name"},"properties":{"consortiumManagementAccountPassword":"consortiumManagementAccountPassword","consortium":"consortium","dns":"dns","consortiumRole":"consortiumRole","provisioningState":"NotSpecified","publicKey":"publicKey","userName":"userName","consortiumMemberDisplayName":"consortiumMemberDisplayName","password":"password","protocol":"NotSpecified","consortiumManagementAccountAddress":"consortiumManagementAccountAddress","firewallRules":[{"endIpAddress":"endIpAddress","ruleName":"ruleName","startIpAddress":"startIpAddress"},{"endIpAddress":"endIpAddress","ruleName":"ruleName","startIpAddress":"startIpAddress"}],"validatorNodesSku":{"capacity":0},"rootContractAddress":"rootContractAddress"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}'.format(blockchain_member_name='blockchain_member_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=blockchain_member,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blockchain_members_delete(client):
    """Test case for blockchain_members_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}'.format(blockchain_member_name='blockchain_member_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blockchain_members_get(client):
    """Test case for blockchain_members_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}'.format(blockchain_member_name='blockchain_member_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blockchain_members_list(client):
    """Test case for blockchain_members_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blockchain_members_list_all(client):
    """Test case for blockchain_members_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Blockchain/blockchainMembers'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blockchain_members_list_api_keys(client):
    """Test case for blockchain_members_list_api_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}/listApiKeys'.format(blockchain_member_name='blockchain_member_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blockchain_members_list_consortium_members(client):
    """Test case for blockchain_members_list_consortium_members

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}/consortiumMembers'.format(blockchain_member_name='blockchain_member_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blockchain_members_list_regenerate_api_keys(client):
    """Test case for blockchain_members_list_regenerate_api_keys

    
    """
    api_key = {"keyName":"keyName","value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}/regenerateApiKeys'.format(blockchain_member_name='blockchain_member_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=api_key,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blockchain_members_update(client):
    """Test case for blockchain_members_update

    
    """
    blockchain_member = {"properties":{"consortiumManagementAccountPassword":"consortiumManagementAccountPassword"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}'.format(blockchain_member_name='blockchain_member_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=blockchain_member,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

