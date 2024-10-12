# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_definition import JobDefinition
from openapi_server.models.job_definition_list import JobDefinitionList
from openapi_server.models.run_parameters import RunParameters


pytestmark = pytest.mark.asyncio

async def test_job_definitions_create_or_update(client):
    """Test case for job_definitions_create_or_update

    
    """
    job_definition = {"properties":{"dataSourceId":"dataSourceId","lastModifiedTime":"2000-01-23T04:56:07.000+00:00","dataServiceInput":"{}","schedules":[{"policyList":["policyList","policyList"],"name":"name"},{"policyList":["policyList","policyList"],"name":"name"}],"customerSecrets":[{"keyIdentifier":"keyIdentifier","keyValue":"keyValue","algorithm":"None"},{"keyIdentifier":"keyIdentifier","keyValue":"keyValue","algorithm":"None"}],"dataSinkId":"dataSinkId","runLocation":"none","state":"Disabled","userConfirmation":"NotRequired"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataServices/{data_service_name}/jobDefinitions/{job_definition_name}'.format(data_service_name='data_service_name_example', job_definition_name='job_definition_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        json=job_definition,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_definitions_delete(client):
    """Test case for job_definitions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataServices/{data_service_name}/jobDefinitions/{job_definition_name}'.format(data_service_name='data_service_name_example', job_definition_name='job_definition_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_definitions_get(client):
    """Test case for job_definitions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataServices/{data_service_name}/jobDefinitions/{job_definition_name}'.format(data_service_name='data_service_name_example', job_definition_name='job_definition_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_definitions_list_by_data_manager(client):
    """Test case for job_definitions_list_by_data_manager

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/jobDefinitions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_definitions_list_by_data_service(client):
    """Test case for job_definitions_list_by_data_service

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataServices/{data_service_name}/jobDefinitions'.format(data_service_name='data_service_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_definitions_run(client):
    """Test case for job_definitions_run

    
    """
    run_parameters = {"dataServiceInput":"{}","customerSecrets":[{"keyIdentifier":"keyIdentifier","keyValue":"keyValue","algorithm":"None"},{"keyIdentifier":"keyIdentifier","keyValue":"keyValue","algorithm":"None"}],"userConfirmation":"NotRequired"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataServices/{data_service_name}/jobDefinitions/{job_definition_name}/run'.format(data_service_name='data_service_name_example', job_definition_name='job_definition_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        json=run_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

