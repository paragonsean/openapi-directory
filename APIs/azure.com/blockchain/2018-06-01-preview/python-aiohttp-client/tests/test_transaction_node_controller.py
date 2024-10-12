# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.api_key_collection import ApiKeyCollection
from openapi_server.models.transaction_node import TransactionNode
from openapi_server.models.transaction_node_collection import TransactionNodeCollection
from openapi_server.models.transaction_node_update import TransactionNodeUpdate


pytestmark = pytest.mark.asyncio

async def test_transaction_nodes_create(client):
    """Test case for transaction_nodes_create

    
    """
    transaction_node = {"location":"location","properties":{"password":"password","dns":"dns","provisioningState":"NotSpecified","publicKey":"publicKey","userName":"userName","firewallRules":[{"endIpAddress":"endIpAddress","ruleName":"ruleName","startIpAddress":"startIpAddress"},{"endIpAddress":"endIpAddress","ruleName":"ruleName","startIpAddress":"startIpAddress"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}/transactionNodes/{transaction_node_name}'.format(blockchain_member_name='blockchain_member_name_example', transaction_node_name='transaction_node_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=transaction_node,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_nodes_delete(client):
    """Test case for transaction_nodes_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}/transactionNodes/{transaction_node_name}'.format(blockchain_member_name='blockchain_member_name_example', transaction_node_name='transaction_node_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_nodes_get(client):
    """Test case for transaction_nodes_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}/transactionNodes/{transaction_node_name}'.format(blockchain_member_name='blockchain_member_name_example', transaction_node_name='transaction_node_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_nodes_list(client):
    """Test case for transaction_nodes_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}/transactionNodes'.format(blockchain_member_name='blockchain_member_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_nodes_list_api_keys(client):
    """Test case for transaction_nodes_list_api_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}/transactionNodes/{transaction_node_name}/listApiKeys'.format(blockchain_member_name='blockchain_member_name_example', transaction_node_name='transaction_node_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_nodes_list_regenerate_api_keys(client):
    """Test case for transaction_nodes_list_regenerate_api_keys

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}/transactionNodes/{transaction_node_name}/regenerateApiKeys'.format(blockchain_member_name='blockchain_member_name_example', transaction_node_name='transaction_node_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=api_key,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_nodes_update(client):
    """Test case for transaction_nodes_update

    
    """
    transaction_node = {"properties":{"password":"password","firewallRules":[{"endIpAddress":"endIpAddress","ruleName":"ruleName","startIpAddress":"startIpAddress"},{"endIpAddress":"endIpAddress","ruleName":"ruleName","startIpAddress":"startIpAddress"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Blockchain/blockchainMembers/{blockchain_member_name}/transactionNodes/{transaction_node_name}'.format(blockchain_member_name='blockchain_member_name_example', transaction_node_name='transaction_node_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=transaction_node,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

