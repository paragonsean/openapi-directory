# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.environment_create_or_update_parameters import EnvironmentCreateOrUpdateParameters
from openapi_server.models.environment_list_response import EnvironmentListResponse
from openapi_server.models.environment_resource import EnvironmentResource
from openapi_server.models.standard_environment_update_parameters import StandardEnvironmentUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_environments_create_or_update(client):
    """Test case for environments_create_or_update

    
    """
    parameters = {"kind":"Standard","sku":{"name":"S1","capacity":1}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_delete(client):
    """Test case for environments_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_get(client):
    """Test case for environments_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_list_by_resource_group(client):
    """Test case for environments_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_list_by_subscription(client):
    """Test case for environments_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.TimeSeriesInsights/environments'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_update(client):
    """Test case for environments_update

    
    """
    standard_environment_update_parameters = {"sku":{"name":"S1","capacity":1},"properties":{"partitionKeyProperties":[{"name":"name","type":"String"},{"name":"name","type":"String"}],"storageLimitExceededBehavior":"PurgeOldData","dataRetentionTime":"dataRetentionTime"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example'),
        headers=headers,
        json=standard_environment_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

