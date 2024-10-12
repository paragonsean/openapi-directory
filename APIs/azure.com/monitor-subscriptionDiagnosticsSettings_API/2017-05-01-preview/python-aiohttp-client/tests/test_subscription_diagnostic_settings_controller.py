# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.subscription_diagnostic_settings_resource import SubscriptionDiagnosticSettingsResource
from openapi_server.models.subscription_diagnostic_settings_resource_collection import SubscriptionDiagnosticSettingsResourceCollection


pytestmark = pytest.mark.asyncio

async def test_subscription_diagnostic_settings_create_or_update(client):
    """Test case for subscription_diagnostic_settings_create_or_update

    
    """
    parameters = {"properties":{"serviceBusRuleId":"serviceBusRuleId","storageAccountId":"storageAccountId","eventHubAuthorizationRuleId":"eventHubAuthorizationRuleId","eventHubName":"eventHubName","logs":[{"category":"category","enabled":True},{"category":"category","enabled":True}],"workspaceId":"workspaceId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/diagnosticSettings/{name}'.format(subscription_id='subscription_id_example', name='name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_diagnostic_settings_delete(client):
    """Test case for subscription_diagnostic_settings_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/diagnosticSettings/{name}'.format(subscription_id='subscription_id_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_diagnostic_settings_get(client):
    """Test case for subscription_diagnostic_settings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/diagnosticSettings/{name}'.format(subscription_id='subscription_id_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_diagnostic_settings_list(client):
    """Test case for subscription_diagnostic_settings_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/diagnosticSettings'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

