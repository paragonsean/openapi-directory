# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.anonymization_data import AnonymizationData
from openapi_server.models.export_set_id import ExportSetId
from openapi_server.models.image import Image
from openapi_server.models.image_attribute import ImageAttribute
from openapi_server.models.image_information import ImageInformation
from openapi_server.models.images_post_request import ImagesPostRequest
from openapi_server.models.tag_mapping import TagMapping


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_images_delete_post(client):
    """Test case for images_delete_post

    
    """
    image_ids = [56]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/images/delete',
        headers=headers,
        json=image_ids,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_export_get(client):
    """Test case for images_export_get

    
    """
    params = [('id', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/images/export',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_images_export_post(client):
    """Test case for images_export_post

    
    """
    image_ids = [56]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/images/export',
        headers=headers,
        json=image_ids,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_images_id_anonymize_put_0(client):
    """Test case for images_id_anonymize_put_0

    
    """
    tag_values = openapi_server.AnonymizationData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/images/{id}/anonymize'.format(id=56),
        headers=headers,
        json=tag_values,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_images_id_anonymized_post_0(client):
    """Test case for images_id_anonymized_post_0

    
    """
    tag_values = openapi_server.AnonymizationData()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/images/{id}/anonymized'.format(id=56),
        headers=headers,
        json=tag_values,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_id_attributes_get(client):
    """Test case for images_id_attributes_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/images/{id}/attributes'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_id_delete(client):
    """Test case for images_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/images/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_id_get(client):
    """Test case for images_id_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/images/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_id_imageinformation_get(client):
    """Test case for images_id_imageinformation_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/images/{id}/imageinformation'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_images_id_modify_put(client):
    """Test case for images_id_modify_put

    
    """
    tag_path_value_mappings = [openapi_server.TagMapping()]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/images/{id}/modify'.format(id=56),
        headers=headers,
        json=tag_path_value_mappings,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_id_png_get(client):
    """Test case for images_id_png_get

    
    """
    params = [('framenumber', 1),
                    ('windowmin', 0),
                    ('windowmax', 0),
                    ('imageheight', 0)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/images/{id}/png'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_images_jpeg_post(client):
    """Test case for images_jpeg_post

    
    """
    jpeg_bytes = None
    params = [('studyid', 56),
                    ('description', 'description_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/images/jpeg',
        headers=headers,
        json=jpeg_bytes,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_images_post(client):
    """Test case for images_post

    
    """
    body = openapi_server.ImagesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/images',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

