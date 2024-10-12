# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.role_definition import RoleDefinition
from openapi_server.models.role_definition_list_result import RoleDefinitionListResult


pytestmark = pytest.mark.asyncio

async def test_role_definitions_create_or_update(client):
    """Test case for role_definitions_create_or_update

    
    """
    role_definition = {"name":"name","id":"id","type":"type","properties":{"permissions":[{"notActions":["notActions","notActions"],"dataActions":["dataActions","dataActions"],"notDataActions":["notDataActions","notDataActions"],"actions":["actions","actions"]},{"notActions":["notActions","notActions"],"dataActions":["dataActions","dataActions"],"notDataActions":["notDataActions","notDataActions"],"actions":["actions","actions"]}],"roleName":"roleName","description":"description","type":"type","assignableScopes":["assignableScopes","assignableScopes"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.Authorization/roleDefinitions/{role_definition_id}'.format(scope='scope_example', role_definition_id='role_definition_id_example'),
        headers=headers,
        json=role_definition,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_definitions_delete(client):
    """Test case for role_definitions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.Authorization/roleDefinitions/{role_definition_id}'.format(scope='scope_example', role_definition_id='role_definition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_definitions_get(client):
    """Test case for role_definitions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Authorization/roleDefinitions/{role_definition_id}'.format(scope='scope_example', role_definition_id='role_definition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_definitions_list(client):
    """Test case for role_definitions_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Authorization/roleDefinitions'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

