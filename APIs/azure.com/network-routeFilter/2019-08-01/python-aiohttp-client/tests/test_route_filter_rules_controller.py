# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.patch_route_filter_rule import PatchRouteFilterRule
from openapi_server.models.route_filter_rule import RouteFilterRule
from openapi_server.models.route_filter_rule_list_result import RouteFilterRuleListResult


pytestmark = pytest.mark.asyncio

async def test_route_filter_rules_create_or_update(client):
    """Test case for route_filter_rules_create_or_update

    
    """
    route_filter_rule_parameters = {"name":"name","etag":"etag","location":"location","properties":{"access":"Allow","routeFilterRuleType":"Community","provisioningState":"Succeeded","communities":["communities","communities"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeFilters/{route_filter_name}/routeFilterRules/{rule_name}'.format(resource_group_name='resource_group_name_example', route_filter_name='route_filter_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=route_filter_rule_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_filter_rules_delete(client):
    """Test case for route_filter_rules_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeFilters/{route_filter_name}/routeFilterRules/{rule_name}'.format(resource_group_name='resource_group_name_example', route_filter_name='route_filter_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_filter_rules_get(client):
    """Test case for route_filter_rules_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeFilters/{route_filter_name}/routeFilterRules/{rule_name}'.format(resource_group_name='resource_group_name_example', route_filter_name='route_filter_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_filter_rules_list_by_route_filter(client):
    """Test case for route_filter_rules_list_by_route_filter

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeFilters/{route_filter_name}/routeFilterRules'.format(resource_group_name='resource_group_name_example', route_filter_name='route_filter_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_filter_rules_update(client):
    """Test case for route_filter_rules_update

    
    """
    route_filter_rule_parameters = {"name":"name","etag":"etag","properties":{"access":"Allow","routeFilterRuleType":"Community","provisioningState":"Succeeded","communities":["communities","communities"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeFilters/{route_filter_name}/routeFilterRules/{rule_name}'.format(resource_group_name='resource_group_name_example', route_filter_name='route_filter_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=route_filter_rule_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

