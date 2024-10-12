# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.generic_error import GenericError
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.image_metadata import ImageMetadata


pytestmark = pytest.mark.asyncio

async def test_image_delete_images_id_delete(client):
    """Test case for image_delete_images_id_delete

    Delete image
    """
    headers = { 
        'Accept': 'application/json',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/images/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_image_list_all_images_get(client):
    """Test case for image_list_all_images_get

    List all images
    """
    headers = { 
        'Accept': 'application/json',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/images',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_image_list_images_id_get(client):
    """Test case for image_list_images_id_get

    List image
    """
    headers = { 
        'Accept': 'application/json',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/images/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_image_upload_images_post(client):
    """Test case for image_upload_images_post

    Upload image
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'RapidAPI': 'special-key',
    }
    data = FormData()
    data.add_field('image', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/images',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

