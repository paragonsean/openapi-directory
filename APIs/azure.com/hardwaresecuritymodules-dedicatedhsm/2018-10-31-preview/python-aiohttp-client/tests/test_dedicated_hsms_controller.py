# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dedicated_hsm import DedicatedHsm
from openapi_server.models.dedicated_hsm_error import DedicatedHsmError
from openapi_server.models.dedicated_hsm_list_result import DedicatedHsmListResult
from openapi_server.models.dedicated_hsm_patch_parameters import DedicatedHsmPatchParameters


pytestmark = pytest.mark.asyncio

async def test_dedicated_hsm_create_or_update(client):
    """Test case for dedicated_hsm_create_or_update

    
    """
    parameters = {"properties":{"stampId":"stampId","networkProfile":{"subnet":{"id":"id"},"networkInterfaces":[{"id":"id","privateIpAddress":"privateIpAddress"},{"id":"id","privateIpAddress":"privateIpAddress"}]},"provisioningState":"Succeeded","statusMessage":"statusMessage"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_hsm_delete(client):
    """Test case for dedicated_hsm_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_hsm_get(client):
    """Test case for dedicated_hsm_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_hsm_list_by_resource_group(client):
    """Test case for dedicated_hsm_list_by_resource_group

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_hsm_list_by_subscription(client):
    """Test case for dedicated_hsm_list_by_subscription

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_hsm_update(client):
    """Test case for dedicated_hsm_update

    
    """
    parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

