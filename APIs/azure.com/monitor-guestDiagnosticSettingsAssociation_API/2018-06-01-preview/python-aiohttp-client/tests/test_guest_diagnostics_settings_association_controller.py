# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.guest_diagnostic_settings_association_resource import GuestDiagnosticSettingsAssociationResource


pytestmark = pytest.mark.asyncio

async def test_guest_diagnostics_settings_association_create_or_update(client):
    """Test case for guest_diagnostics_settings_association_create_or_update

    
    """
    diagnostic_settings_association = {"properties":{"guestDiagnosticSettingsName":"guestDiagnosticSettingsName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{resource_uri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{association_name}'.format(resource_uri='resource_uri_example', association_name='association_name_example'),
        headers=headers,
        json=diagnostic_settings_association,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_guest_diagnostics_settings_association_delete(client):
    """Test case for guest_diagnostics_settings_association_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{resource_uri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{association_name}'.format(resource_uri='resource_uri_example', association_name='association_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_guest_diagnostics_settings_association_get(client):
    """Test case for guest_diagnostics_settings_association_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_uri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{association_name}'.format(resource_uri='resource_uri_example', association_name='association_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

