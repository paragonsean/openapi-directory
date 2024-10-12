# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.reference_data_set_create_or_update_parameters import ReferenceDataSetCreateOrUpdateParameters
from openapi_server.models.reference_data_set_list_response import ReferenceDataSetListResponse
from openapi_server.models.reference_data_set_resource import ReferenceDataSetResource
from openapi_server.models.reference_data_set_update_parameters import ReferenceDataSetUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_reference_data_sets_create_or_update(client):
    """Test case for reference_data_sets_create_or_update

    
    """
    parameters = {"properties":{"dataStringComparisonBehavior":"Ordinal","keyProperties":[{"name":"name","type":"String"},{"name":"name","type":"String"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/referenceDataSets/{reference_data_set_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example', reference_data_set_name='reference_data_set_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reference_data_sets_delete(client):
    """Test case for reference_data_sets_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/referenceDataSets/{reference_data_set_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example', reference_data_set_name='reference_data_set_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reference_data_sets_get(client):
    """Test case for reference_data_sets_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/referenceDataSets/{reference_data_set_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example', reference_data_set_name='reference_data_set_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reference_data_sets_list_by_environment(client):
    """Test case for reference_data_sets_list_by_environment

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/referenceDataSets'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reference_data_sets_update(client):
    """Test case for reference_data_sets_update

    
    """
    reference_data_set_update_parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/referenceDataSets/{reference_data_set_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example', reference_data_set_name='reference_data_set_name_example'),
        headers=headers,
        json=reference_data_set_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

