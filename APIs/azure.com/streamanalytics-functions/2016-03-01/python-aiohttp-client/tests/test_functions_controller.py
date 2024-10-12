# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.function import Function
from openapi_server.models.function_list_result import FunctionListResult
from openapi_server.models.function_retrieve_default_definition_parameters import FunctionRetrieveDefaultDefinitionParameters
from openapi_server.models.functions_test200_response import FunctionsTest200Response


pytestmark = pytest.mark.asyncio

async def test_functions_create_or_replace(client):
    """Test case for functions_create_or_replace

    
    """
    function = {"properties":{"etag":"etag","type":"type"}}
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
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/functions/{function_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', function_name='function_name_example'),
        headers=headers,
        json=function,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_delete(client):
    """Test case for functions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/functions/{function_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', function_name='function_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_get(client):
    """Test case for functions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/functions/{function_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', function_name='function_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_list_by_streaming_job(client):
    """Test case for functions_list_by_streaming_job

    
    """
    params = [('$select', 'select_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/functions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_retrieve_default_definition(client):
    """Test case for functions_retrieve_default_definition

    
    """
    function_retrieve_default_definition_parameters = {"bindingType":"bindingType"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/functions/{function_name}/RetrieveDefaultDefinition'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', function_name='function_name_example'),
        headers=headers,
        json=function_retrieve_default_definition_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_test(client):
    """Test case for functions_test

    
    """
    function = {"properties":{"etag":"etag","type":"type"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/functions/{function_name}/test'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', function_name='function_name_example'),
        headers=headers,
        json=function,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_update(client):
    """Test case for functions_update

    
    """
    function = {"properties":{"etag":"etag","type":"type"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/functions/{function_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', function_name='function_name_example'),
        headers=headers,
        json=function,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

