# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_package import APIPagedResponseUpdateSystemModelsPackage
from openapi_server.models.update_system_models_package import UpdateSystemModelsPackage


pytestmark = pytest.mark.asyncio

async def test_packages_delete_package(client):
    """Test case for packages_delete_package

    Delete a Package.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/Packages/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_packages_get_package(client):
    """Test case for packages_get_package

    Find a Package.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Packages/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_packages_get_packages(client):
    """Test case for packages_get_packages

    List Packages.
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('PackageTypeID', 'package_type_id_example'),
                    ('Version', 56),
                    ('Released', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Packages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_packages_post_package(client):
    """Test case for packages_post_package

    Add a Package to the Update System.
    """
    body = openapi_server.UpdateSystemModelsPackage()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/Packages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_packages_put_package(client):
    """Test case for packages_put_package

    Modify a Packge to the Update System.
    """
    body = openapi_server.UpdateSystemModelsPackage()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Packages/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

