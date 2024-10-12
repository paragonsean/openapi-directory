# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.managed_rule_set_definition_list import ManagedRuleSetDefinitionList


pytestmark = pytest.mark.asyncio

async def test_managed_rule_sets_list(client):
    """Test case for managed_rule_sets_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallManagedRuleSets'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

