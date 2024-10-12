# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.view_list_result import ViewListResult
from openapi_server.models.view_resource_format import ViewResourceFormat


pytestmark = pytest.mark.asyncio

async def test_views_create_or_update(client):
    """Test case for views_create_or_update

    
    """
    parameters = {"properties":{"viewName":"viewName","created":"2000-01-23T04:56:07.000+00:00","displayName":{"key":"displayName"},"tenantId":"tenantId","definition":"definition","userId":"userId","changed":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/views/{view_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', view_name='view_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_delete(client):
    """Test case for views_delete

    
    """
    params = [('api-version', 'api_version_example'),
                    ('userId', 'user_id_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/views/{view_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', view_name='view_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_get(client):
    """Test case for views_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/views/{view_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', view_name='view_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_list_by_hub(client):
    """Test case for views_list_by_hub

    
    """
    params = [('api-version', 'api_version_example'),
                    ('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/views'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

