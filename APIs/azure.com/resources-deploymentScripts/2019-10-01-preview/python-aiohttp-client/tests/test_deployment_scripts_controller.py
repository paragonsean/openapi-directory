# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_response import DefaultErrorResponse
from openapi_server.models.deployment_script import DeploymentScript
from openapi_server.models.deployment_script_list_result import DeploymentScriptListResult
from openapi_server.models.deployment_script_update_parameter import DeploymentScriptUpdateParameter
from openapi_server.models.script_log import ScriptLog
from openapi_server.models.script_logs_list import ScriptLogsList


pytestmark = pytest.mark.asyncio

async def test_deployment_scripts_create(client):
    """Test case for deployment_scripts_create

    
    """
    deployment_script = {"identity":{"userAssignedIdentities":{"key":{"clientId":"clientId","principalId":"principalId"}},"type":"UserAssigned"},"kind":"AzurePowerShell","location":"location","tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deploymentScripts/{script_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', script_name='script_name_example'),
        headers=headers,
        json=deployment_script,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_scripts_delete(client):
    """Test case for deployment_scripts_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deploymentScripts/{script_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', script_name='script_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_scripts_get(client):
    """Test case for deployment_scripts_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deploymentScripts/{script_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', script_name='script_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_scripts_get_logs(client):
    """Test case for deployment_scripts_get_logs

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deploymentScripts/{script_name}/logs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', script_name='script_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_scripts_get_logs_default(client):
    """Test case for deployment_scripts_get_logs_default

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deploymentScripts/{script_name}/logs/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', script_name='script_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_scripts_list_by_resource_group(client):
    """Test case for deployment_scripts_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deploymentScripts'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_scripts_list_by_subscription(client):
    """Test case for deployment_scripts_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Resources/deploymentScripts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_scripts_update(client):
    """Test case for deployment_scripts_update

    
    """
    deployment_script = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deploymentScripts/{script_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', script_name='script_name_example'),
        headers=headers,
        json=deployment_script,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

