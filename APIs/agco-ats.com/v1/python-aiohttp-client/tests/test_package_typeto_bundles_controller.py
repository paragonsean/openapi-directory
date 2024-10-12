# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_package_type_i_dto_bundle import APIPagedResponseUpdateSystemModelsPackageTypeIDtoBundle
from openapi_server.models.update_system_models_package_type_i_dto_bundle import UpdateSystemModelsPackageTypeIDtoBundle


pytestmark = pytest.mark.asyncio

async def test_package_typeto_bundles_delete(client):
    """Test case for package_typeto_bundles_delete

    Delete a Package Type to Bundle Relationship.
    """
    params = [('BundleID', 'bundle_id_example'),
                    ('PackageTypeID', 'package_type_id_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/PackageTypetoBundles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_typeto_bundles_get(client):
    """Test case for package_typeto_bundles_get

    Get all of the Package Type to Bundle Relationships.
    """
    params = [('BundleID', 'bundle_id_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/PackageTypetoBundles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_package_typeto_bundles_post(client):
    """Test case for package_typeto_bundles_post

    Add a new Package Type ID to Bundle Relationship.
    """
    body = openapi_server.UpdateSystemModelsPackageTypeIDtoBundle()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/PackageTypetoBundles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_package_typeto_bundles_put(client):
    """Test case for package_typeto_bundles_put

    Update a Package Type ID to Bundle Relationship.
    """
    body = openapi_server.UpdateSystemModelsPackageTypeIDtoBundle()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/PackageTypetoBundles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

