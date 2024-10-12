# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.web_application_firewall_policy import WebApplicationFirewallPolicy
from openapi_server.models.web_application_firewall_policy_list import WebApplicationFirewallPolicyList


pytestmark = pytest.mark.asyncio

async def test_policies_create_or_update(client):
    """Test case for policies_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"customRules":{"rules":[{"enabledState":"Disabled","ruleType":"MatchRule","name":"name","action":"Allow","rateLimitDurationInMinutes":3,"matchConditions":[{"transforms":["Lowercase","Lowercase"],"matchValue":["matchValue","matchValue"],"selector":"selector","matchVariable":"RemoteAddr","negateCondition":True,"operator":"Any"},{"transforms":["Lowercase","Lowercase"],"matchValue":["matchValue","matchValue"],"selector":"selector","matchVariable":"RemoteAddr","negateCondition":True,"operator":"Any"}],"priority":0,"rateLimitThreshold":0},{"enabledState":"Disabled","ruleType":"MatchRule","name":"name","action":"Allow","rateLimitDurationInMinutes":3,"matchConditions":[{"transforms":["Lowercase","Lowercase"],"matchValue":["matchValue","matchValue"],"selector":"selector","matchVariable":"RemoteAddr","negateCondition":True,"operator":"Any"},{"transforms":["Lowercase","Lowercase"],"matchValue":["matchValue","matchValue"],"selector":"selector","matchVariable":"RemoteAddr","negateCondition":True,"operator":"Any"}],"priority":0,"rateLimitThreshold":0}]},"frontendEndpointLinks":[{"id":"id"},{"id":"id"}],"policySettings":{"mode":"Prevention","enabledState":"Disabled","redirectUrl":"redirectUrl","customBlockResponseStatusCode":5,"customBlockResponseBody":"customBlockResponseBody"},"resourceState":"Creating","provisioningState":"provisioningState","managedRules":{"managedRuleSets":[{"ruleSetVersion":"ruleSetVersion","ruleSetType":"ruleSetType","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"ruleGroupOverrides":[{"ruleGroupName":"ruleGroupName","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"rules":[{"enabledState":"Disabled","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"ruleId":"ruleId"},{"enabledState":"Disabled","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"ruleId":"ruleId"}]},{"ruleGroupName":"ruleGroupName","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"rules":[{"enabledState":"Disabled","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"ruleId":"ruleId"},{"enabledState":"Disabled","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"ruleId":"ruleId"}]}]},{"ruleSetVersion":"ruleSetVersion","ruleSetType":"ruleSetType","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"ruleGroupOverrides":[{"ruleGroupName":"ruleGroupName","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"rules":[{"enabledState":"Disabled","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"ruleId":"ruleId"},{"enabledState":"Disabled","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"ruleId":"ruleId"}]},{"ruleGroupName":"ruleGroupName","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"rules":[{"enabledState":"Disabled","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"ruleId":"ruleId"},{"enabledState":"Disabled","exclusions":[{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"},{"selector":"selector","selectorMatchOperator":"Equals","matchVariable":"RequestHeaderNames"}],"ruleId":"ruleId"}]}]}]}}}
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


pytestmark = pytest.mark.asyncio

async def test_policies_delete(client):
    """Test case for policies_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies/{policy_name}'.format(resource_group_name='resource_group_name_example', policy_name='policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_get(client):
    """Test case for policies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies/{policy_name}'.format(resource_group_name='resource_group_name_example', policy_name='policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policies_list(client):
    """Test case for policies_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

