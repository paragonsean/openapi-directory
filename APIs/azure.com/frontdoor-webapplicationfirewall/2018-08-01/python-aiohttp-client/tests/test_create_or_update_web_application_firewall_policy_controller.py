# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.web_application_firewall_policy import WebApplicationFirewallPolicy


pytestmark = pytest.mark.asyncio

async def test_policies_create_or_update(client):
    """Test case for policies_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"customRules":{"rules":[{"ruleType":"MatchRule","name":"name","transforms":["Lowercase","Lowercase"],"action":"Allow","etag":"etag","rateLimitDurationInMinutes":6,"matchConditions":[{"matchValue":["matchValue","matchValue"],"selector":"selector","matchVariable":"RemoteAddr","negateCondition":True,"operator":"Any"},{"matchValue":["matchValue","matchValue"],"selector":"selector","matchVariable":"RemoteAddr","negateCondition":True,"operator":"Any"}],"priority":0,"rateLimitThreshold":1},{"ruleType":"MatchRule","name":"name","transforms":["Lowercase","Lowercase"],"action":"Allow","etag":"etag","rateLimitDurationInMinutes":6,"matchConditions":[{"matchValue":["matchValue","matchValue"],"selector":"selector","matchVariable":"RemoteAddr","negateCondition":True,"operator":"Any"},{"matchValue":["matchValue","matchValue"],"selector":"selector","matchVariable":"RemoteAddr","negateCondition":True,"operator":"Any"}],"priority":0,"rateLimitThreshold":1}]},"policySettings":{"mode":"Prevention","enabledState":"Disabled"},"resourceState":"Creating","provisioningState":"provisioningState","managedRules":{"ruleSets":[{"ruleSetType":"ruleSetType","priority":5,"version":5},{"ruleSetType":"ruleSetType","priority":5,"version":5}]}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies/{policy_name}'.format(resource_group_name='resource_group_name_example', policy_name='policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

