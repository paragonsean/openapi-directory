# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.secret_value import SecretValue
from openapi_server.models.secret_value_resource_description import SecretValueResourceDescription
from openapi_server.models.secret_value_resource_description_list import SecretValueResourceDescriptionList


pytestmark = pytest.mark.asyncio

async def test_secret_value_create(client):
    """Test case for secret_value_create

    Adds the specified value as a new version of the specified secret resource.
    """
    secret_value_resource_description = {"properties":{"provisioningState":"provisioningState","value":"value"}}
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/secrets/{secret_resource_name}/values/{secret_value_resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', secret_resource_name='secret_resource_name_example', secret_value_resource_name='secret_value_resource_name_example'),
        headers=headers,
        json=secret_value_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secret_value_delete(client):
    """Test case for secret_value_delete

    Deletes the specified  value of the named secret resource.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/secrets/{secret_resource_name}/values/{secret_value_resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', secret_resource_name='secret_resource_name_example', secret_value_resource_name='secret_value_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secret_value_get(client):
    """Test case for secret_value_get

    Gets the specified secret value resource.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/secrets/{secret_resource_name}/values/{secret_value_resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', secret_resource_name='secret_resource_name_example', secret_value_resource_name='secret_value_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secret_value_list(client):
    """Test case for secret_value_list

    List names of all values of the specified secret resource.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/secrets/{secret_resource_name}/values'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', secret_resource_name='secret_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secret_value_list_value(client):
    """Test case for secret_value_list_value

    Lists the specified value of the secret resource.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/secrets/{secret_resource_name}/values/{secret_value_resource_name}/list_value'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', secret_resource_name='secret_resource_name_example', secret_value_resource_name='secret_value_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

