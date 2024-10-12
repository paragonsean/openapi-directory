# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.rule import Rule
from openapi_server.models.rule_list_result import RuleListResult


pytestmark = pytest.mark.asyncio

async def test_rules_create_or_update(client):
    """Test case for rules_create_or_update

    
    """
    parameters = {"properties":{"correlationFilter":{"replyToSessionId":"replyToSessionId","requiresPreprocessing":True,"replyTo":"replyTo","messageId":"messageId","correlationId":"correlationId","label":"label","sessionId":"sessionId","to":"to","contentType":"contentType","properties":{"key":"properties"}},"sqlFilter":{"compatibilityLevel":20,"requiresPreprocessing":True,"sqlExpression":"sqlExpression"},"action":{"compatibilityLevel":0,"requiresPreprocessing":True,"sqlExpression":"sqlExpression"},"filterType":"SqlFilter"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/subscriptions/{subscription_name}/rules/{rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', subscription_name='subscription_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rules_delete(client):
    """Test case for rules_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/subscriptions/{subscription_name}/rules/{rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', subscription_name='subscription_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rules_list_by_subscriptions(client):
    """Test case for rules_list_by_subscriptions

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skip', 56),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/subscriptions/{subscription_name}/rules'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', subscription_name='subscription_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

