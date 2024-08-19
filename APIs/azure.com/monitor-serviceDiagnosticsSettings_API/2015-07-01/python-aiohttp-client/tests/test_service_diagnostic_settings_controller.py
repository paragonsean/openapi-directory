# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.service_diagnostic_settings_resource import ServiceDiagnosticSettingsResource


pytestmark = pytest.mark.asyncio

async def test_service_diagnostic_settings_create_or_update(client):
    """Test case for service_diagnostic_settings_create_or_update

    
    """
    parameters = {"properties":{"serviceBusRuleId":"serviceBusRuleId","storageAccountId":"storageAccountId","metrics":[{"timeGrain":"timeGrain","retentionPolicy":{"days":0,"enabled":True},"enabled":True},{"timeGrain":"timeGrain","retentionPolicy":{"days":0,"enabled":True},"enabled":True}],"logs":[{"retentionPolicy":{"days":0,"enabled":True},"category":"category","enabled":True},{"retentionPolicy":{"days":0,"enabled":True},"category":"category","enabled":True}],"workspaceId":"workspaceId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{resource_uri}/providers/microsoft.insights/diagnosticSettings/service'.format(resource_uri='resource_uri_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_diagnostic_settings_get(client):
    """Test case for service_diagnostic_settings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_uri}/providers/microsoft.insights/diagnosticSettings/service'.format(resource_uri='resource_uri_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

