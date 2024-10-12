# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.failover_group import FailoverGroup
from openapi_server.models.failover_group_list_result import FailoverGroupListResult
from openapi_server.models.failover_group_update import FailoverGroupUpdate


pytestmark = pytest.mark.asyncio

async def test_failover_groups_create_or_update(client):
    """Test case for failover_groups_create_or_update

    
    """
    parameters = {"location":"location","properties":{"replicationRole":"Primary","databases":["databases","databases"],"replicationState":"replicationState","partnerServers":[{"replicationRole":"Primary","location":"location","id":"id"},{"replicationRole":"Primary","location":"location","id":"id"}],"readOnlyEndpoint":{"failoverPolicy":"Disabled"},"readWriteEndpoint":{"failoverWithDataLossGracePeriodMinutes":0,"failoverPolicy":"Manual"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/failoverGroups/{failover_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', failover_group_name='failover_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_failover_groups_delete(client):
    """Test case for failover_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/failoverGroups/{failover_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', failover_group_name='failover_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_failover_groups_failover(client):
    """Test case for failover_groups_failover

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/failoverGroups/{failover_group_name}/failover'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', failover_group_name='failover_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_failover_groups_force_failover_allow_data_loss(client):
    """Test case for failover_groups_force_failover_allow_data_loss

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/failoverGroups/{failover_group_name}/forceFailoverAllowDataLoss'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', failover_group_name='failover_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_failover_groups_get(client):
    """Test case for failover_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/failoverGroups/{failover_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', failover_group_name='failover_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_failover_groups_list_by_server(client):
    """Test case for failover_groups_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/failoverGroups'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_failover_groups_update(client):
    """Test case for failover_groups_update

    
    """
    parameters = {"properties":{"databases":["databases","databases"],"readOnlyEndpoint":{"failoverPolicy":"Disabled"},"readWriteEndpoint":{"failoverWithDataLossGracePeriodMinutes":0,"failoverPolicy":"Manual"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/failoverGroups/{failover_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', failover_group_name='failover_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

