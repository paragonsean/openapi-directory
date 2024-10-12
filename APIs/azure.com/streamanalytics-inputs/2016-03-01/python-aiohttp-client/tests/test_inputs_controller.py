# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.input import Input
from openapi_server.models.input_list_result import InputListResult
from openapi_server.models.resource_test_status import ResourceTestStatus


pytestmark = pytest.mark.asyncio

async def test_inputs_create_or_replace(client):
    """Test case for inputs_create_or_replace

    
    """
    input = {"properties":{"serialization":{"type":"type"},"diagnostics":{"conditions":[{"code":"code","message":"message","since":"since"},{"code":"code","message":"message","since":"since"}]},"etag":"etag","type":"type"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/inputs/{input_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', input_name='input_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inputs_delete(client):
    """Test case for inputs_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/inputs/{input_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', input_name='input_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inputs_get(client):
    """Test case for inputs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/inputs/{input_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', input_name='input_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inputs_list_by_streaming_job(client):
    """Test case for inputs_list_by_streaming_job

    
    """
    params = [('$select', 'select_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/inputs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inputs_test(client):
    """Test case for inputs_test

    
    """
    input = {"properties":{"serialization":{"type":"type"},"diagnostics":{"conditions":[{"code":"code","message":"message","since":"since"},{"code":"code","message":"message","since":"since"}]},"etag":"etag","type":"type"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/inputs/{input_name}/test'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', input_name='input_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inputs_update(client):
    """Test case for inputs_update

    
    """
    input = {"properties":{"serialization":{"type":"type"},"diagnostics":{"conditions":[{"code":"code","message":"message","since":"since"},{"code":"code","message":"message","since":"since"}]},"etag":"etag","type":"type"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/inputs/{input_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', input_name='input_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

