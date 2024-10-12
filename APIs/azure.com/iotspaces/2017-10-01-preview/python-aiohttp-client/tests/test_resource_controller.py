# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.io_t_spaces_description import IoTSpacesDescription
from openapi_server.models.io_t_spaces_patch_description import IoTSpacesPatchDescription


pytestmark = pytest.mark.asyncio

async def test_io_t_spaces_create_or_update(client):
    """Test case for io_t_spaces_create_or_update

    
    """
    iot_space_description = {"sku":{"name":"F1"},"properties":{"storageContainer":{"connectionString":"connectionString","resourceGroup":"resourceGroup","containerName":"containerName","subscriptionId":"subscriptionId"},"provisioningState":"Provisioning","managementApiUrl":"managementApiUrl","webPortalUrl":"webPortalUrl"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.IoTSpaces/Graph/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=iot_space_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_io_t_spaces_delete(client):
    """Test case for io_t_spaces_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.IoTSpaces/Graph/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_io_t_spaces_get(client):
    """Test case for io_t_spaces_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.IoTSpaces/Graph/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_io_t_spaces_update(client):
    """Test case for io_t_spaces_update

    
    """
    iot_space_patch_description = {"properties":{"storageContainer":{"connectionString":"connectionString","resourceGroup":"resourceGroup","containerName":"containerName","subscriptionId":"subscriptionId"},"provisioningState":"Provisioning","managementApiUrl":"managementApiUrl","webPortalUrl":"webPortalUrl"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.IoTSpaces/Graph/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=iot_space_patch_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

