# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_global_image_category import APIIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_global_image_category import GlobalResourcesSharedModelsGlobalImageCategory


pytestmark = pytest.mark.asyncio

async def test_global_image_categories_get_file(client):
    """Test case for global_image_categories_get_file

    Gets a file's metadata.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/GlobalImageCategories/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_image_categories_get_files(client):
    """Test case for global_image_categories_get_files

    Get a paged response of file metadata.
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/GlobalImageCategories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_global_image_categories_post_file(client):
    """Test case for global_image_categories_post_file

    Create the metadata for a file before uploading. The State should be 'Created'.
    """
    body = openapi_server.GlobalResourcesSharedModelsGlobalImageCategory()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/GlobalImageCategories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

