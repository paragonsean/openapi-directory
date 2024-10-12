# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.showback_rule import ShowbackRule
from openapi_server.models.showback_rule_list_result import ShowbackRuleListResult


pytestmark = pytest.mark.asyncio

async def test_showback_rule_create_update_rule(client):
    """Test case for showback_rule_create_update_rule

    
    """
    showback_rule = {"name":"name","id":"id","type":"type","properties":{"creationTime":"2000-01-23T04:56:07.000+00:00","modificationTime":"2000-01-23T04:56:07.000+00:00","ruleType":"CustomPrice","description":"description","deprecationTime":"2000-01-23T04:56:07.000+00:00","scopes":[{"name":"name","id":"id","type":"type"},{"name":"name","id":"id","type":"type"}],"version":0,"status":"NotActive"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.CostManagement/showbackRules/{rule_name}'.format(billing_account_id='billing_account_id_example', rule_name='rule_name_example'),
        headers=headers,
        json=showback_rule,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_showback_rule_get_billing_account_id(client):
    """Test case for showback_rule_get_billing_account_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.CostManagement/showbackRules/{rule_name}'.format(billing_account_id='billing_account_id_example', rule_name='rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_showback_rules_list(client):
    """Test case for showback_rules_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.CostManagement/showbackRules'.format(billing_account_id='billing_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

