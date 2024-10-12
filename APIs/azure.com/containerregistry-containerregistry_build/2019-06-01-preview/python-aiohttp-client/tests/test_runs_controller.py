# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.run import Run
from openapi_server.models.run_get_log_result import RunGetLogResult
from openapi_server.models.run_list_result import RunListResult
from openapi_server.models.run_update_parameters import RunUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_runs_cancel(client):
    """Test case for runs_cancel

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/runs/{run_id}/cancel'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', run_id='run_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runs_get(client):
    """Test case for runs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/runs/{run_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', run_id='run_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runs_get_log_sas_url(client):
    """Test case for runs_get_log_sas_url

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/runs/{run_id}/listLogSasUrl'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', run_id='run_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runs_list(client):
    """Test case for runs_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/runs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runs_update(client):
    """Test case for runs_update

    
    """
    run_update_parameters = {"isArchiveEnabled":True}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/runs/{run_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', run_id='run_id_example'),
        headers=headers,
        json=run_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

