# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_package_type import APIPagedResponseUpdateSystemModelsPackageType
from openapi_server.models.update_system_models_package_type import UpdateSystemModelsPackageType


pytestmark = pytest.mark.asyncio

async def test_api_v2_package_types_idget(client):
    """Test case for api_v2_package_types_idget

    Get a specific Package Type.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/PackageTypes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_types_add_package_type_user(client):
    """Test case for package_types_add_package_type_user

    Add a package type that a user can see.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/PackageTypes/{id}/Users/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_types_delete(client):
    """Test case for package_types_delete

    Delete a Package Type.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/PackageTypes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_types_get(client):
    """Test case for package_types_get

    Get all of the Package Types.
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('userID', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/PackageTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_package_types_post(client):
    """Test case for package_types_post

    Add a Package Type.
    """
    body = openapi_server.UpdateSystemModelsPackageType()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/PackageTypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_package_types_put(client):
    """Test case for package_types_put

    Modify a Package Type.
    """
    body = openapi_server.UpdateSystemModelsPackageType()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/PackageTypes/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_types_remove_package_type_user(client):
    """Test case for package_types_remove_package_type_user

    Deletes a package type a user could see.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/PackageTypes/{id}/Users/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

