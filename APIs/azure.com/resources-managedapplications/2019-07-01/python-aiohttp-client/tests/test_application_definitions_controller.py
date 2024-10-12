# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_definition import ApplicationDefinition
from openapi_server.models.application_definition_list_result import ApplicationDefinitionListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_application_definitions_create_or_update(client):
    """Test case for application_definitions_create_or_update

    
    """
    parameters = {"properties":{"notificationPolicy":{"notificationEndpoints":[{"uri":"uri"},{"uri":"uri"}]},"managementPolicy":{"mode":"NotSpecified"},"displayName":"displayName","lockLevel":"CanNotDelete","packageFileUri":"packageFileUri","authorizations":[{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"},{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"}],"policies":[{"policyDefinitionId":"policyDefinitionId","name":"name","parameters":"parameters"},{"policyDefinitionId":"policyDefinitionId","name":"name","parameters":"parameters"}],"description":"description","lockingPolicy":{"allowedActions":["allowedActions","allowedActions"]},"deploymentPolicy":{"deploymentMode":"NotSpecified"},"mainTemplate":"{}","createUiDefinition":"{}","isEnabled":True,"artifacts":[{"name":"NotSpecified","type":"NotSpecified","uri":"uri"},{"name":"NotSpecified","type":"NotSpecified","uri":"uri"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applicationDefinitions/{application_definition_name}'.format(resource_group_name='resource_group_name_example', application_definition_name='application_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_definitions_delete(client):
    """Test case for application_definitions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applicationDefinitions/{application_definition_name}'.format(resource_group_name='resource_group_name_example', application_definition_name='application_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_definitions_get(client):
    """Test case for application_definitions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applicationDefinitions/{application_definition_name}'.format(resource_group_name='resource_group_name_example', application_definition_name='application_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_definitions_list_by_resource_group(client):
    """Test case for application_definitions_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applicationDefinitions'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

