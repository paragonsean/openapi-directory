# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.registration_assignment import RegistrationAssignment
from openapi_server.models.registration_assignment_list import RegistrationAssignmentList


pytestmark = pytest.mark.asyncio

async def test_registration_assignments_create_or_update(client):
    """Test case for registration_assignments_create_or_update

    
    """
    request_body = {"name":"name","id":"id","type":"type","properties":{"registrationDefinitionId":"registrationDefinitionId","provisioningState":"NotSpecified","registrationDefinition":{"name":"name","id":"id","type":"type","plan":{"product":"product","name":"name","publisher":"publisher","version":"version"},"properties":{"manageeTenantName":"manageeTenantName","manageeTenantId":"manageeTenantId","registrationDefinitionName":"registrationDefinitionName","managedByTenantId":"managedByTenantId","authorizations":[{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"},{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"}],"description":"description","provisioningState":"NotSpecified","managedByTenantName":"managedByTenantName"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.ManagedServices/registrationAssignments/{registration_assignment_id}'.format(scope='scope_example', registration_assignment_id='registration_assignment_id_example'),
        headers=headers,
        json=request_body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registration_assignments_delete(client):
    """Test case for registration_assignments_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.ManagedServices/registrationAssignments/{registration_assignment_id}'.format(scope='scope_example', registration_assignment_id='registration_assignment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registration_assignments_get(client):
    """Test case for registration_assignments_get

    
    """
    params = [('$expandRegistrationDefinition', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.ManagedServices/registrationAssignments/{registration_assignment_id}'.format(scope='scope_example', registration_assignment_id='registration_assignment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registration_assignments_list(client):
    """Test case for registration_assignments_list

    
    """
    params = [('$expandRegistrationDefinition', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.ManagedServices/registrationAssignments'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

