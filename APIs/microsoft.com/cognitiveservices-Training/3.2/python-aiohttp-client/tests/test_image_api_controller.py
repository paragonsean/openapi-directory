# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.image import Image
from openapi_server.models.image_create_summary import ImageCreateSummary
from openapi_server.models.image_file_create_batch import ImageFileCreateBatch
from openapi_server.models.image_id_create_batch import ImageIdCreateBatch
from openapi_server.models.image_region_create_batch import ImageRegionCreateBatch
from openapi_server.models.image_region_create_summary import ImageRegionCreateSummary
from openapi_server.models.image_tag_create_batch import ImageTagCreateBatch
from openapi_server.models.image_tag_create_summary import ImageTagCreateSummary
from openapi_server.models.image_url_create_batch import ImageUrlCreateBatch
from openapi_server.models.suggested_tag_and_region_query import SuggestedTagAndRegionQuery
from openapi_server.models.suggested_tag_and_region_query_token import SuggestedTagAndRegionQueryToken
from openapi_server.models.tag_filter import TagFilter


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_image_regions(client):
    """Test case for create_image_regions

    Create a set of image regions.
    """
    body = {"regions":[{"imageId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","top":7.0614014,"left":2.302136,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":9.301444,"height":5.637377},{"imageId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","top":7.0614014,"left":2.302136,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":9.301444,"height":5.637377}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.2/training/projects/{project_id}/images/regions'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_image_tags(client):
    """Test case for create_image_tags

    Associate a set of images with a set of tags.
    """
    body = {"tags":[{"imageId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"imageId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.2/training/projects/{project_id}/images/tags'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_images_from_data(client):
    """Test case for create_images_from_data

    Add the provided images to the set of training images.
    """
    params = [('tagIds', ['[\"b607964f-7bd6-4a3b-a869-6791fb6aab87\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'apim_key': 'special-key',
    }
    data = FormData()
    data.add_field('image_data', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/customvision/v3.2/training/projects/{project_id}/images'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_images_from_files(client):
    """Test case for create_images_from_files

    Add the provided batch of images to the set of training images.
    """
    body = {"images":[{"regions":[{"top":1.4658129,"left":6.0274563,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":5.962134,"height":0.8008282},{"top":1.4658129,"left":6.0274563,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":5.962134,"height":0.8008282}],"contents":"contents","tagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name"},{"regions":[{"top":1.4658129,"left":6.0274563,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":5.962134,"height":0.8008282},{"top":1.4658129,"left":6.0274563,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":5.962134,"height":0.8008282}],"contents":"contents","tagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name"}],"tagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.2/training/projects/{project_id}/images/files'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_images_from_predictions(client):
    """Test case for create_images_from_predictions

    Add the specified predicted images to the set of training images.
    """
    body = {"images":[{"regions":[{"top":1.4658129,"left":6.0274563,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":5.962134,"height":0.8008282},{"top":1.4658129,"left":6.0274563,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":5.962134,"height":0.8008282}],"tagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"regions":[{"top":1.4658129,"left":6.0274563,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":5.962134,"height":0.8008282},{"top":1.4658129,"left":6.0274563,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":5.962134,"height":0.8008282}],"tagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}],"tagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.2/training/projects/{project_id}/images/predictions'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_images_from_urls(client):
    """Test case for create_images_from_urls

    Add the provided images urls to the set of training images.
    """
    body = {"images":[{"regions":[{"top":1.4658129,"left":6.0274563,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":5.962134,"height":0.8008282},{"top":1.4658129,"left":6.0274563,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":5.962134,"height":0.8008282}],"tagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"url":"url"},{"regions":[{"top":1.4658129,"left":6.0274563,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":5.962134,"height":0.8008282},{"top":1.4658129,"left":6.0274563,"tagId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","width":5.962134,"height":0.8008282}],"tagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"url":"url"}],"tagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.2/training/projects/{project_id}/images/urls'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_image_regions(client):
    """Test case for delete_image_regions

    Delete a set of image regions.
    """
    params = [('regionIds', ['[\"\"]'])]
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/customvision/v3.2/training/projects/{project_id}/images/regions'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_image_tags(client):
    """Test case for delete_image_tags

    Remove a set of tags from a set of images.
    """
    params = [('imageIds', ['[\"e31a14ab-5d78-4f7b-a267-3a1e4fd8a758\",\"cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12\"]']),
                    ('tagIds', ['[\"e31a14ab-5d78-4f7b-a267-3a1e4fd8a758\",\"cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12\"]'])]
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/customvision/v3.2/training/projects/{project_id}/images/tags'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_images(client):
    """Test case for delete_images

    Delete images from the set of training images.
    """
    params = [('imageIds', ['[\"e31a14ab-5d78-4f7b-a267-3a1e4fd8a758\",\"cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12\"]']),
                    ('allImages', True),
                    ('allIterations', True)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/customvision/v3.2/training/projects/{project_id}/images'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_images_by_ids(client):
    """Test case for get_images_by_ids

    Get images by id for a given project iteration.
    """
    params = [('imageIds', ['image_ids_example']),
                    ('iterationId', 'cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v3.2/training/projects/{project_id}/images/id'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tagged_image_count(client):
    """Test case for get_tagged_image_count

    Gets the number of images tagged with the provided {tagIds}.
    """
    params = [('iterationId', 'cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12'),
                    ('tagIds', ['tag_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v3.2/training/projects/{project_id}/images/tagged/count'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tagged_images(client):
    """Test case for get_tagged_images

    Get tagged images for a given project iteration.
    """
    params = [('iterationId', 'cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12'),
                    ('tagIds', ['tag_ids_example']),
                    ('orderBy', 'order_by_example'),
                    ('take', 50),
                    ('skip', 0)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v3.2/training/projects/{project_id}/images/tagged'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_untagged_image_count(client):
    """Test case for get_untagged_image_count

    Gets the number of untagged images.
    """
    params = [('iterationId', 'cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v3.2/training/projects/{project_id}/images/untagged/count'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_untagged_images(client):
    """Test case for get_untagged_images

    Get untagged images for a given project iteration.
    """
    params = [('iterationId', 'cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12'),
                    ('orderBy', 'order_by_example'),
                    ('take', 50),
                    ('skip', 0)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v3.2/training/projects/{project_id}/images/untagged'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_query_suggested_image_count(client):
    """Test case for query_suggested_image_count

    Get count of images whose suggested tags match given tags and their probabilities are greater than or equal to the given threshold. Returns count as 0 if none found.
    """
    body = {"tagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"threshold":0.8008281904610115}
    params = [('iterationId', 'b7b9d99c-a2c6-4658-9900-a98d2ff5bc66')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.2/training/projects/{project_id}/images/suggested/count'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_query_suggested_images(client):
    """Test case for query_suggested_images

    Get untagged images whose suggested tags match given tags. Returns empty array if no images are found.
    """
    body = {"session":"session","tagIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"sortBy":"UncertaintyAscending","threshold":2.027123023002322,"continuation":"continuation","maxCount":3}
    params = [('iterationId', 'b7b9d99c-a2c6-4658-9900-a98d2ff5bc66')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.2/training/projects/{project_id}/images/suggested'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

