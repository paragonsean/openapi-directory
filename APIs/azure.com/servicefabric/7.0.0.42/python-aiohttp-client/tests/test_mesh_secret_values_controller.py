# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_secret_value_resource_description_list import PagedSecretValueResourceDescriptionList
from openapi_server.models.secret_value import SecretValue
from openapi_server.models.secret_value_resource_description import SecretValueResourceDescription


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_mesh_secret_value_add_value(client):
    """Test case for mesh_secret_value_add_value

    Adds the specified value as a new version of the specified secret resource.
    """
    secret_value_resource_description = openapi_server.SecretValueResourceDescription()
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/Resources/Secrets/{secret_resource_name}/values/{secret_value_resource_name}'.format(secret_resource_name='secret_resource_name_example', secret_value_resource_name='secret_value_resource_name_example'),
        headers=headers,
        json=secret_value_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_secret_value_delete(client):
    """Test case for mesh_secret_value_delete

    Deletes the specified  value of the named secret resource.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/Resources/Secrets/{secret_resource_name}/values/{secret_value_resource_name}'.format(secret_resource_name='secret_resource_name_example', secret_value_resource_name='secret_value_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_secret_value_get(client):
    """Test case for mesh_secret_value_get

    Gets the specified secret value resource.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Secrets/{secret_resource_name}/values/{secret_value_resource_name}'.format(secret_resource_name='secret_resource_name_example', secret_value_resource_name='secret_value_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_secret_value_list(client):
    """Test case for mesh_secret_value_list

    List names of all values of the specified secret resource.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Secrets/{secret_resource_name}/values'.format(secret_resource_name='secret_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_secret_value_show(client):
    """Test case for mesh_secret_value_show

    Lists the specified value of the secret resource.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Resources/Secrets/{secret_resource_name}/values/{secret_value_resource_name}/list_value'.format(secret_resource_name='secret_resource_name_example', secret_value_resource_name='secret_value_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

