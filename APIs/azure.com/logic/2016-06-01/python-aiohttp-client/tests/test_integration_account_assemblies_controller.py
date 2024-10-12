# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assembly_collection import AssemblyCollection
from openapi_server.models.assembly_definition import AssemblyDefinition
from openapi_server.models.workflow_trigger_callback_url import WorkflowTriggerCallbackUrl


pytestmark = pytest.mark.asyncio

async def test_integration_account_assemblies_create_or_update(client):
    """Test case for integration_account_assemblies_create_or_update

    
    """
    assembly_artifact = {"properties":{"assemblyName":"assemblyName","assemblyPublicKeyToken":"assemblyPublicKeyToken","assemblyCulture":"assemblyCulture","assemblyVersion":"assemblyVersion"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/assemblies/{assembly_artifact_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', assembly_artifact_name='assembly_artifact_name_example'),
        headers=headers,
        json=assembly_artifact,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_account_assemblies_delete(client):
    """Test case for integration_account_assemblies_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/assemblies/{assembly_artifact_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', assembly_artifact_name='assembly_artifact_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_account_assemblies_get(client):
    """Test case for integration_account_assemblies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/assemblies/{assembly_artifact_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', assembly_artifact_name='assembly_artifact_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_account_assemblies_list(client):
    """Test case for integration_account_assemblies_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/assemblies'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_account_assemblies_list_content_callback_url(client):
    """Test case for integration_account_assemblies_list_content_callback_url

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/assemblies/{assembly_artifact_name}/listContentCallbackUrl'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', assembly_artifact_name='assembly_artifact_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

