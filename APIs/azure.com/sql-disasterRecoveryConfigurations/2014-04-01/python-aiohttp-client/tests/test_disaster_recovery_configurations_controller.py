# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.disaster_recovery_configuration import DisasterRecoveryConfiguration
from openapi_server.models.disaster_recovery_configuration_list_result import DisasterRecoveryConfigurationListResult


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configurations_create_or_update(client):
    """Test case for disaster_recovery_configurations_create_or_update

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/disasterRecoveryConfiguration/{disaster_recovery_configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', disaster_recovery_configuration_name='disaster_recovery_configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configurations_delete(client):
    """Test case for disaster_recovery_configurations_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/disasterRecoveryConfiguration/{disaster_recovery_configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', disaster_recovery_configuration_name='disaster_recovery_configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configurations_failover(client):
    """Test case for disaster_recovery_configurations_failover

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/disasterRecoveryConfiguration/{disaster_recovery_configuration_name}/failover'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', disaster_recovery_configuration_name='disaster_recovery_configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configurations_failover_allow_data_loss(client):
    """Test case for disaster_recovery_configurations_failover_allow_data_loss

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/disasterRecoveryConfiguration/{disaster_recovery_configuration_name}/forceFailoverAllowDataLoss'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', disaster_recovery_configuration_name='disaster_recovery_configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configurations_get(client):
    """Test case for disaster_recovery_configurations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/disasterRecoveryConfiguration/{disaster_recovery_configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', disaster_recovery_configuration_name='disaster_recovery_configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configurations_list(client):
    """Test case for disaster_recovery_configurations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/disasterRecoveryConfiguration'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

