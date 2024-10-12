# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.service_diagnostic_settings_resource import ServiceDiagnosticSettingsResource
from openapi_server.models.service_diagnostic_settings_resource_patch import ServiceDiagnosticSettingsResourcePatch


pytestmark = pytest.mark.asyncio

async def test_service_diagnostic_settings_update(client):
    """Test case for service_diagnostic_settings_update

    
    """
    service_diagnostic_settings_resource = {"properties":{"serviceBusRuleId":"serviceBusRuleId","storageAccountId":"storageAccountId","eventHubAuthorizationRuleId":"eventHubAuthorizationRuleId","metrics":[{"timeGrain":"timeGrain","retentionPolicy":{"days":0,"enabled":True},"enabled":True},{"timeGrain":"timeGrain","retentionPolicy":{"days":0,"enabled":True},"enabled":True}],"logs":[{"retentionPolicy":{"days":0,"enabled":True},"category":"category","enabled":True},{"retentionPolicy":{"days":0,"enabled":True},"category":"category","enabled":True}],"workspaceId":"workspaceId"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/{resource_uri}/providers/microsoft.insights/diagnosticSettings/service'.format(resource_uri='resource_uri_example'),
        headers=headers,
        json=service_diagnostic_settings_resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

