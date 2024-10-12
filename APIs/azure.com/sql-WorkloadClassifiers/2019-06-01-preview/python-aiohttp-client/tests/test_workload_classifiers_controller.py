# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.workload_classifier import WorkloadClassifier
from openapi_server.models.workload_classifier_list_result import WorkloadClassifierListResult


pytestmark = pytest.mark.asyncio

async def test_workload_classifiers_create_or_update(client):
    """Test case for workload_classifiers_create_or_update

    
    """
    parameters = {"properties":{"importance":"importance","context":"context","memberName":"memberName","startTime":"startTime","endTime":"endTime","label":"label"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/workloadGroups/{workload_group_name}/workloadClassifiers/{workload_classifier_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', workload_group_name='workload_group_name_example', workload_classifier_name='workload_classifier_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workload_classifiers_delete(client):
    """Test case for workload_classifiers_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/workloadGroups/{workload_group_name}/workloadClassifiers/{workload_classifier_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', workload_group_name='workload_group_name_example', workload_classifier_name='workload_classifier_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workload_classifiers_get(client):
    """Test case for workload_classifiers_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/workloadGroups/{workload_group_name}/workloadClassifiers/{workload_classifier_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', workload_group_name='workload_group_name_example', workload_classifier_name='workload_classifier_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workload_classifiers_list_by_workload_group(client):
    """Test case for workload_classifiers_list_by_workload_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/workloadGroups/{workload_group_name}/workloadClassifiers'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', workload_group_name='workload_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

