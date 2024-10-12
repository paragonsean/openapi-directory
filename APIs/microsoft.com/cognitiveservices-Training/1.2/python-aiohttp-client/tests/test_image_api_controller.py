# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.image import Image
from openapi_server.models.image_create_summary import ImageCreateSummary
from openapi_server.models.image_file_create_batch import ImageFileCreateBatch
from openapi_server.models.image_id_create_batch import ImageIdCreateBatch
from openapi_server.models.image_tag_create_batch import ImageTagCreateBatch
from openapi_server.models.image_tag_create_summary import ImageTagCreateSummary
from openapi_server.models.image_url_create_batch import ImageUrlCreateBatch


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_images_from_data(client):
    """Test case for create_images_from_data

    Add the provided images to the set of training images
    """
    params = [('tagIds', ['[\"b607964f-7bd6-4a3b-a869-6791fb6aab87\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'training_key': '{API Key}',
    }
    data = FormData()
    data.add_field('image_data', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/customvision/v1.2/Training/projects/{project_id}/images'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_images_from_files(client):
    """Test case for create_images_from_files

    Add the provided batch of images to the set of training images
    """
    body = {"TagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"Images":[{"Contents":"Contents","TagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"Name":"Name"},{"Contents":"Contents","TagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"Name":"Name"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v1.2/Training/projects/{project_id}/images/files'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_images_from_predictions(client):
    """Test case for create_images_from_predictions

    Add the specified predicted images to the set of training images
    """
    body = {"TagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"Images":[{"TagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"TagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v1.2/Training/projects/{project_id}/images/predictions'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_images_from_urls(client):
    """Test case for create_images_from_urls

    Add the provided images urls to the set of training images
    """
    body = {"TagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"Images":[{"TagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"Url":"Url"},{"TagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"Url":"Url"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v1.2/Training/projects/{project_id}/images/urls'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_image_tags(client):
    """Test case for delete_image_tags

    Remove a set of tags from a set of images
    """
    params = [('imageIds', ['[\"e31a14ab-5d78-4f7b-a267-3a1e4fd8a758\",\"cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12\"]']),
                    ('tagIds', ['[\"e31a14ab-5d78-4f7b-a267-3a1e4fd8a758\",\"cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12\"]'])]
    headers = { 
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='DELETE',
        path='/customvision/v1.2/Training/projects/{project_id}/images/tags'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_images(client):
    """Test case for delete_images

    Delete images from the set of training images
    """
    params = [('imageIds', ['[\"e31a14ab-5d78-4f7b-a267-3a1e4fd8a758\",\"cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12\"]'])]
    headers = { 
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='DELETE',
        path='/customvision/v1.2/Training/projects/{project_id}/images'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tagged_images(client):
    """Test case for get_tagged_images

    Get tagged images for a given project iteration
    """
    params = [('iterationId', 'cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12'),
                    ('tagIds', ['tag_ids_example']),
                    ('orderBy', 'order_by_example'),
                    ('take', 50),
                    ('skip', 0)]
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v1.2/Training/projects/{project_id}/images/tagged'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_untagged_images(client):
    """Test case for get_untagged_images

    Get untagged images for a given project iteration
    """
    params = [('iterationId', 'cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12'),
                    ('orderBy', 'order_by_example'),
                    ('take', 50),
                    ('skip', 0)]
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v1.2/Training/projects/{project_id}/images/untagged'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_image_tags(client):
    """Test case for post_image_tags

    Associate a set of images with a set of tags
    """
    body = {"Tags":[{"ImageId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","TagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"ImageId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","TagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v1.2/Training/projects/{project_id}/images/tags'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

