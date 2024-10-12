# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert_rule_resource import AlertRuleResource
from openapi_server.models.alert_rule_resource_collection import AlertRuleResourceCollection
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_alert_rules_create_or_update(client):
    """Test case for alert_rules_create_or_update

    
    """
    parameters = {"properties":{"condition":{"odata.type":"odata.type","dataSource":{"odata.type":"odata.type","resourceUri":"resourceUri"}},"isEnabled":True,"name":"name","description":"description","lastUpdatedTime":"2000-01-23T04:56:07.000+00:00","actions":[{"odata.type":"odata.type"},{"odata.type":"odata.type"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/alertrules/{rule_name}'.format(resource_group_name='resource_group_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alert_rules_delete(client):
    """Test case for alert_rules_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/alertrules/{rule_name}'.format(resource_group_name='resource_group_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alert_rules_get(client):
    """Test case for alert_rules_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/alertrules/{rule_name}'.format(resource_group_name='resource_group_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alert_rules_list_by_resource_group(client):
    """Test case for alert_rules_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/alertrules'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alert_rules_list_by_subscription(client):
    """Test case for alert_rules_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/alertrules'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

