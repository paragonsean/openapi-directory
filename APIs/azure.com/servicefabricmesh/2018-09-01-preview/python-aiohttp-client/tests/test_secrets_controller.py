# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.secret_resource_description import SecretResourceDescription
from openapi_server.models.secret_resource_description_list import SecretResourceDescriptionList


pytestmark = pytest.mark.asyncio

async def test_secret_create(client):
    """Test case for secret_create

    Creates or updates a secret resource.
    """
    secret_resource_description = {"properties":{"description":"description","statusDetails":"statusDetails","contentType":"contentType","status":"Unknown"}}
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/secrets/{secret_resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', secret_resource_name='secret_resource_name_example'),
        headers=headers,
        json=secret_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secret_delete(client):
    """Test case for secret_delete

    Deletes the secret resource.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/secrets/{secret_resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', secret_resource_name='secret_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secret_get(client):
    """Test case for secret_get

    Gets the secret resource with the given name.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/secrets/{secret_resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', secret_resource_name='secret_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secret_list_by_resource_group(client):
    """Test case for secret_list_by_resource_group

    Gets all the secret resources in a given resource group.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/secrets'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secret_list_by_subscription(client):
    """Test case for secret_list_by_subscription

    Gets all the secret resources in a given subscription.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ServiceFabricMesh/secrets'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

