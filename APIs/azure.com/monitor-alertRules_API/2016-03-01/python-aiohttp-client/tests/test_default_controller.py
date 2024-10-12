# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert_rule_resource import AlertRuleResource
from openapi_server.models.alert_rule_resource_patch import AlertRuleResourcePatch
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_alert_rules_update(client):
    """Test case for alert_rules_update

    
    """
    alert_rules_resource = {"properties":{"condition":{"odata.type":"odata.type","dataSource":{"odata.type":"odata.type","resourceUri":"resourceUri"}},"isEnabled":True,"name":"name","description":"description","lastUpdatedTime":"2000-01-23T04:56:07.000+00:00","actions":[{"odata.type":"odata.type"},{"odata.type":"odata.type"}]},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/alertrules/{rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', rule_name='rule_name_example'),
        headers=headers,
        json=alert_rules_resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

