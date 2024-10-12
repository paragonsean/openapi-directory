# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_secret_resource_description_list import PagedSecretResourceDescriptionList
from openapi_server.models.secret_resource_description import SecretResourceDescription


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_mesh_secret_create_or_update(client):
    """Test case for mesh_secret_create_or_update

    Creates or updates a Secret resource.
    """
    secret_resource_description = openapi_server.SecretResourceDescription()
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/Resources/Secrets/{secret_resource_name}'.format(secret_resource_name='secret_resource_name_example'),
        headers=headers,
        json=secret_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_secret_delete(client):
    """Test case for mesh_secret_delete

    Deletes the Secret resource.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/Resources/Secrets/{secret_resource_name}'.format(secret_resource_name='secret_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_secret_get(client):
    """Test case for mesh_secret_get

    Gets the Secret resource with the given name.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Secrets/{secret_resource_name}'.format(secret_resource_name='secret_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_secret_list(client):
    """Test case for mesh_secret_list

    Lists all the secret resources.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Secrets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

