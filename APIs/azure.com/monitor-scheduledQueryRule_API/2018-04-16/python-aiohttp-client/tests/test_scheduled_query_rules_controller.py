# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.log_search_rule_resource import LogSearchRuleResource
from openapi_server.models.log_search_rule_resource_collection import LogSearchRuleResourceCollection
from openapi_server.models.log_search_rule_resource_patch import LogSearchRuleResourcePatch


pytestmark = pytest.mark.asyncio

async def test_scheduled_query_rules_create_or_update(client):
    """Test case for scheduled_query_rules_create_or_update

    
    """
    parameters = {"properties":{"schedule":{"frequencyInMinutes":0,"timeWindowInMinutes":6},"action":{"odata.type":"odata.type"},"description":"description","lastUpdatedTime":"2000-01-23T04:56:07.000+00:00","provisioningState":"Succeeded","source":{"dataSourceId":"dataSourceId","authorizedResources":["authorizedResources","authorizedResources"],"query":"query","queryType":"ResultCount"},"enabled":"true"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/scheduledQueryRules/{rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', rule_name='rule_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scheduled_query_rules_delete(client):
    """Test case for scheduled_query_rules_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/scheduledQueryRules/{rule_name}'.format(resource_group_name='resource_group_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scheduled_query_rules_get(client):
    """Test case for scheduled_query_rules_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/scheduledQueryRules/{rule_name}'.format(resource_group_name='resource_group_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scheduled_query_rules_list_by_resource_group(client):
    """Test case for scheduled_query_rules_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/scheduledQueryRules'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scheduled_query_rules_list_by_subscription(client):
    """Test case for scheduled_query_rules_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/scheduledQueryRules'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scheduled_query_rules_update(client):
    """Test case for scheduled_query_rules_update

    
    """
    parameters = {"properties":{"enabled":"true"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/scheduledQueryRules/{rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', rule_name='rule_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

