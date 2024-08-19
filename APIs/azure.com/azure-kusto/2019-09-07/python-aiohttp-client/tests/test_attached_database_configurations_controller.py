# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attached_database_configuration import AttachedDatabaseConfiguration
from openapi_server.models.attached_database_configuration_list_result import AttachedDatabaseConfigurationListResult
from openapi_server.models.cloud_error import CloudError


pytestmark = pytest.mark.asyncio

async def test_attached_database_configurations_create_or_update(client):
    """Test case for attached_database_configurations_create_or_update

    
    """
    parameters = {"location":"location","properties":{"databaseName":"databaseName","defaultPrincipalsModificationKind":"Union","attachedDatabaseNames":["attachedDatabaseNames","attachedDatabaseNames"],"provisioningState":"Running","clusterResourceId":"clusterResourceId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/attachedDatabaseConfigurations/{attached_database_configuration_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', attached_database_configuration_name='attached_database_configuration_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attached_database_configurations_delete(client):
    """Test case for attached_database_configurations_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/attachedDatabaseConfigurations/{attached_database_configuration_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', attached_database_configuration_name='attached_database_configuration_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attached_database_configurations_get(client):
    """Test case for attached_database_configurations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/attachedDatabaseConfigurations/{attached_database_configuration_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', attached_database_configuration_name='attached_database_configuration_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attached_database_configurations_list_by_cluster(client):
    """Test case for attached_database_configurations_list_by_cluster

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/attachedDatabaseConfigurations'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

