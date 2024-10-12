# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.registration_definition import RegistrationDefinition
from openapi_server.models.registration_definition_list import RegistrationDefinitionList


pytestmark = pytest.mark.asyncio

async def test_registration_definitions_create_or_update(client):
    """Test case for registration_definitions_create_or_update

    
    """
    request_body = {"name":"name","id":"id","type":"type","plan":{"product":"product","name":"name","publisher":"publisher","version":"version"},"properties":{"registrationDefinitionName":"registrationDefinitionName","managedByTenantId":"managedByTenantId","authorizations":[{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"},{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"}],"description":"description","provisioningState":"NotSpecified","managedByTenantName":"managedByTenantName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.ManagedServices/registrationDefinitions/{registration_definition_id}'.format(registration_definition_id='registration_definition_id_example', scope='scope_example'),
        headers=headers,
        json=request_body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registration_definitions_delete(client):
    """Test case for registration_definitions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.ManagedServices/registrationDefinitions/{registration_definition_id}'.format(registration_definition_id='registration_definition_id_example', scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registration_definitions_get(client):
    """Test case for registration_definitions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.ManagedServices/registrationDefinitions/{registration_definition_id}'.format(scope='scope_example', registration_definition_id='registration_definition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registration_definitions_list(client):
    """Test case for registration_definitions_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.ManagedServices/registrationDefinitions'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

