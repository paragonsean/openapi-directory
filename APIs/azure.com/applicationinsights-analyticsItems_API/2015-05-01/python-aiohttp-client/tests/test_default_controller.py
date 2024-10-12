# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_insights_component_analytics_item import ApplicationInsightsComponentAnalyticsItem


pytestmark = pytest.mark.asyncio

async def test_analytics_items_delete(client):
    """Test case for analytics_items_delete

    
    """
    params = [('api-version', 'api_version_example'),
                    ('id', 'id_example'),
                    ('name', 'name_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/components/{resource_name}/{scope_path}/item'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', scope_path='scope_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_items_get(client):
    """Test case for analytics_items_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('id', 'id_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/components/{resource_name}/{scope_path}/item'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', scope_path='scope_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_items_list(client):
    """Test case for analytics_items_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('scope', shared),
                    ('type', none),
                    ('includeContent', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/components/{resource_name}/{scope_path}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', scope_path='scope_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analytics_items_put(client):
    """Test case for analytics_items_put

    
    """
    item_properties = {"TimeCreated":"TimeCreated","TimeModified":"TimeModified","Type":"query","Scope":"shared","Version":"Version","Content":"Content","Id":"Id","Properties":{"functionAlias":"functionAlias"},"Name":"Name"}
    params = [('api-version', 'api_version_example'),
                    ('overrideItem', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/components/{resource_name}/{scope_path}/item'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', scope_path='scope_path_example'),
        headers=headers,
        json=item_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

