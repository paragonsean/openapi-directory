# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.diagnostic_settings_resource import DiagnosticSettingsResource
from openapi_server.models.diagnostic_settings_resource_collection import DiagnosticSettingsResourceCollection
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_diagnostic_settings_create_or_update(client):
    """Test case for diagnostic_settings_create_or_update

    
    """
    parameters = {"properties":{"serviceBusRuleId":"serviceBusRuleId","storageAccountId":"storageAccountId","eventHubAuthorizationRuleId":"eventHubAuthorizationRuleId","eventHubName":"eventHubName","logs":[{"retentionPolicy":{"days":0,"enabled":True},"category":"AuditLogs","enabled":True},{"retentionPolicy":{"days":0,"enabled":True},"category":"AuditLogs","enabled":True}],"workspaceId":"workspaceId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/microsoft.aadiam/diagnosticSettings/{name}'.format(name='name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostic_settings_delete(client):
    """Test case for diagnostic_settings_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/microsoft.aadiam/diagnosticSettings/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostic_settings_get(client):
    """Test case for diagnostic_settings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/microsoft.aadiam/diagnosticSettings/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostic_settings_list(client):
    """Test case for diagnostic_settings_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/microsoft.aadiam/diagnosticSettings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

