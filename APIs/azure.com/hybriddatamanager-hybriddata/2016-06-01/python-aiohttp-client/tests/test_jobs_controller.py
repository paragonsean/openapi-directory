# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job import Job
from openapi_server.models.job_list import JobList


pytestmark = pytest.mark.asyncio

async def test_jobs_cancel(client):
    """Test case for jobs_cancel

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataServices/{data_service_name}/jobDefinitions/{job_definition_name}/jobs/{job_id}/cancel'.format(data_service_name='data_service_name_example', job_definition_name='job_definition_name_example', job_id='job_id_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_get(client):
    """Test case for jobs_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataServices/{data_service_name}/jobDefinitions/{job_definition_name}/jobs/{job_id}'.format(data_service_name='data_service_name_example', job_definition_name='job_definition_name_example', job_id='job_id_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_list_by_data_manager(client):
    """Test case for jobs_list_by_data_manager

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/jobs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_list_by_data_service(client):
    """Test case for jobs_list_by_data_service

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataServices/{data_service_name}/jobs'.format(data_service_name='data_service_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_list_by_job_definition(client):
    """Test case for jobs_list_by_job_definition

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataServices/{data_service_name}/jobDefinitions/{job_definition_name}/jobs'.format(data_service_name='data_service_name_example', job_definition_name='job_definition_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_resume(client):
    """Test case for jobs_resume

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataServices/{data_service_name}/jobDefinitions/{job_definition_name}/jobs/{job_id}/resume'.format(data_service_name='data_service_name_example', job_definition_name='job_definition_name_example', job_id='job_id_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

