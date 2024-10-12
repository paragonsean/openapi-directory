# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.policy_events_query_results import PolicyEventsQueryResults
from openapi_server.models.query_failure import QueryFailure


pytestmark = pytest.mark.asyncio

async def test_policy_events_list_query_results_for_management_group(client):
    """Test case for policy_events_list_query_results_for_management_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('$select', 'select_example'),
                    ('$from', '2013-10-20T19:20:30+01:00'),
                    ('$to', '2013-10-20T19:20:30+01:00'),
                    ('$filter', 'filter_example'),
                    ('$apply', 'apply_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/{management_groups_namespace}/managementGroups/{management_group_name}/providers/Microsoft.PolicyInsights/policyEvents/{policy_events_resource}/queryResults'.format(policy_events_resource='policy_events_resource_example', management_groups_namespace='management_groups_namespace_example', management_group_name='management_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_events_list_query_results_for_resource(client):
    """Test case for policy_events_list_query_results_for_resource

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('$select', 'select_example'),
                    ('$from', '2013-10-20T19:20:30+01:00'),
                    ('$to', '2013-10-20T19:20:30+01:00'),
                    ('$filter', 'filter_example'),
                    ('$apply', 'apply_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{resource_id}/providers/Microsoft.PolicyInsights/policyEvents/{policy_events_resource}/queryResults'.format(policy_events_resource='policy_events_resource_example', resource_id='resource_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_events_list_query_results_for_resource_group(client):
    """Test case for policy_events_list_query_results_for_resource_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('$select', 'select_example'),
                    ('$from', '2013-10-20T19:20:30+01:00'),
                    ('$to', '2013-10-20T19:20:30+01:00'),
                    ('$filter', 'filter_example'),
                    ('$apply', 'apply_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PolicyInsights/policyEvents/{policy_events_resource}/queryResults'.format(policy_events_resource='policy_events_resource_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_events_list_query_results_for_subscription(client):
    """Test case for policy_events_list_query_results_for_subscription

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('$select', 'select_example'),
                    ('$from', '2013-10-20T19:20:30+01:00'),
                    ('$to', '2013-10-20T19:20:30+01:00'),
                    ('$filter', 'filter_example'),
                    ('$apply', 'apply_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.PolicyInsights/policyEvents/{policy_events_resource}/queryResults'.format(policy_events_resource='policy_events_resource_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

