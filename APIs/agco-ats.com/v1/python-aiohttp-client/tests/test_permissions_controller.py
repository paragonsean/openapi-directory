# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_permission import APIModelsPermission
from openapi_server.models.api_paged_response_api_models_permission import APIPagedResponseAPIModelsPermission


pytestmark = pytest.mark.asyncio

async def test_permissions_delete_permission(client):
    """Test case for permissions_delete_permission

    Deletes a Permission
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/Permissions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permissions_get_permission(client):
    """Test case for permissions_get_permission

    Gets a Permission
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Permissions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permissions_get_permissions(client):
    """Test case for permissions_get_permissions

    List Permissions
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Permissions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_permissions_post_permission(client):
    """Test case for permissions_post_permission

    Adds a Permission
    """
    body = openapi_server.APIModelsPermission()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/Permissions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_permissions_put_permission(client):
    """Test case for permissions_put_permission

    Updates a Permission
    """
    body = openapi_server.APIModelsPermission()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Permissions/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

