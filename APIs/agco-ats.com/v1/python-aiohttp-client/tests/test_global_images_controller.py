# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_global_image import APIIPagedResponseGlobalResourcesSharedModelsGlobalImage
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_global_image import GlobalResourcesSharedModelsGlobalImage


pytestmark = pytest.mark.asyncio

async def test_global_images_delete_file(client):
    """Test case for global_images_delete_file

    Mark a file as 'Removed'. Disables download of the image and hides metadata from GET all method
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/GlobalImages/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_images_get_global_image(client):
    """Test case for global_images_get_global_image

    Gets a GlobalImage's metadata.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/GlobalImages/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_images_get_global_image_contents(client):
    """Test case for global_images_get_global_image_contents

    Download the contents of a GlobalImage. The current State of the GlobalImage should be 'Available'.
    """
    params = [('isFullImage', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/GlobalImages/{id}/ImageContents'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_images_get_global_images(client):
    """Test case for global_images_get_global_images

    Get a paged response of GlobalImage.
    """
    params = [('search', 'search_example'),
                    ('categoryId', 'category_id_example'),
                    ('publisher', 'publisher_example'),
                    ('includeDeleted', True),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/GlobalImages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_global_images_post_global_image(client):
    """Test case for global_images_post_global_image

    Create the metadata for a GlobalImage before uploading. The State should be 'Created'.
    """
    body = openapi_server.GlobalResourcesSharedModelsGlobalImage()
    params = [('overridePublisherOrDate', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/GlobalImages',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_global_images_put_global_image(client):
    """Test case for global_images_put_global_image

    Update the metadata for an image.
    """
    body = openapi_server.GlobalResourcesSharedModelsGlobalImage()
    params = [('overridePublisherOrDate', True)]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/GlobalImages/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_images_put_global_image_contents(client):
    """Test case for global_images_put_global_image_contents

    Upload the contents of a GlobalImage. The current State of the File for the GlobalImage should be 'Created'.
    """
    params = [('isFullImage', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/GlobalImages/{id}/ImageContents'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

