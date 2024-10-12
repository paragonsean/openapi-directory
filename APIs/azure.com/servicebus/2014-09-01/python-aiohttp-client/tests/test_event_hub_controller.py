# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.shared_access_authorization_rule_list_result import SharedAccessAuthorizationRuleListResult
from openapi_server.models.shared_access_authorization_rule_resource import SharedAccessAuthorizationRuleResource


pytestmark = pytest.mark.asyncio

async def test_event_hub_get_authorization_rule(client):
    """Test case for event_hub_get_authorization_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/eventhubs/{eventhub_name}/authorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', eventhub_name='eventhub_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_hub_list_authorization_rules(client):
    """Test case for event_hub_list_authorization_rules

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/eventhubs/{eventhub_name}/authorizationRules'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', eventhub_name='eventhub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

