# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cluster_configurations import ClusterConfigurations
from openapi_server.models.configurations_list_default_response import ConfigurationsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_configurations_get(client):
    """Test case for configurations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/configurations/{configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', configuration_name='configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configurations_list(client):
    """Test case for configurations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/configurations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configurations_update(client):
    """Test case for configurations_update

    
    """
    parameters = {'key': 'parameters_example'}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/configurations/{configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', configuration_name='configuration_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

