# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.guest_diagnostic_settings_association_list import GuestDiagnosticSettingsAssociationList
from openapi_server.models.guest_diagnostic_settings_association_resource import GuestDiagnosticSettingsAssociationResource
from openapi_server.models.guest_diagnostic_settings_association_resource_patch import GuestDiagnosticSettingsAssociationResourcePatch


pytestmark = pytest.mark.asyncio

async def test_guest_diagnostics_settings_association_list(client):
    """Test case for guest_diagnostics_settings_association_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/guestDiagnosticSettingsAssociations'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_guest_diagnostics_settings_association_list_by_resource_group(client):
    """Test case for guest_diagnostics_settings_association_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/guestDiagnosticSettingsAssociations'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_guest_diagnostics_settings_association_update(client):
    """Test case for guest_diagnostics_settings_association_update

    
    """
    parameters = {"properties":{"guestDiagnosticSettingsName":"guestDiagnosticSettingsName"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/{resource_uri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{association_name}'.format(resource_uri='resource_uri_example', association_name='association_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

