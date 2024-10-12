# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_bundle import APIPagedResponseUpdateSystemModelsBundle
from openapi_server.models.update_system_models_bundle import UpdateSystemModelsBundle


pytestmark = pytest.mark.asyncio

async def test_bundles_delete_bundle(client):
    """Test case for bundles_delete_bundle

    Delete a Bundle.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/Bundles/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bundles_get_bundle(client):
    """Test case for bundles_get_bundle

    Get a specific Bundle by ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Bundles/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bundles_get_bundles(client):
    """Test case for bundles_get_bundles

    Get the list of bundles.
    """
    params = [('UpdateGroupID', 'update_group_id_example'),
                    ('Active', True),
                    ('limit', 56),
                    ('offset', 56),
                    ('BundleNumber', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Bundles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bundles_post_bundle(client):
    """Test case for bundles_post_bundle

    Add a Bundle to the Update System.
    """
    body = openapi_server.UpdateSystemModelsBundle()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/Bundles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bundles_put_bundle(client):
    """Test case for bundles_put_bundle

    Modify a Bundle in the Update System.
    """
    body = openapi_server.UpdateSystemModelsBundle()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Bundles/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

