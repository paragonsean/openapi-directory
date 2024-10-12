# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.appliance_definition import ApplianceDefinition
from openapi_server.models.appliance_definition_list_result import ApplianceDefinitionListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_appliance_definitions_create_or_update(client):
    """Test case for appliance_definitions_create_or_update

    
    """
    parameters = {"properties":{"displayName":"displayName","lockLevel":"CanNotDelete","packageFileUri":"packageFileUri","authorizations":[{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"},{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"}],"description":"description","artifacts":[{"name":"name","type":"Template","uri":"uri"},{"name":"name","type":"Template","uri":"uri"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applianceDefinitions/{appliance_definition_name}'.format(resource_group_name='resource_group_name_example', appliance_definition_name='appliance_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliance_definitions_create_or_update_by_id(client):
    """Test case for appliance_definitions_create_or_update_by_id

    
    """
    parameters = {"properties":{"displayName":"displayName","lockLevel":"CanNotDelete","packageFileUri":"packageFileUri","authorizations":[{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"},{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"}],"description":"description","artifacts":[{"name":"name","type":"Template","uri":"uri"},{"name":"name","type":"Template","uri":"uri"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{appliance_definition_id}'.format(appliance_definition_id='appliance_definition_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliance_definitions_delete(client):
    """Test case for appliance_definitions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applianceDefinitions/{appliance_definition_name}'.format(resource_group_name='resource_group_name_example', appliance_definition_name='appliance_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliance_definitions_delete_by_id(client):
    """Test case for appliance_definitions_delete_by_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{appliance_definition_id}'.format(appliance_definition_id='appliance_definition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliance_definitions_get(client):
    """Test case for appliance_definitions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applianceDefinitions/{appliance_definition_name}'.format(resource_group_name='resource_group_name_example', appliance_definition_name='appliance_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliance_definitions_get_by_id(client):
    """Test case for appliance_definitions_get_by_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{appliance_definition_id}'.format(appliance_definition_id='appliance_definition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliance_definitions_list_by_resource_group(client):
    """Test case for appliance_definitions_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applianceDefinitions'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

