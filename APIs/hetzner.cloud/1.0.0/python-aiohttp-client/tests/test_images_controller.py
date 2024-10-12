# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.images_get200_response import ImagesGet200Response
from openapi_server.models.images_id_get200_response import ImagesIdGet200Response
from openapi_server.models.update_image_request import UpdateImageRequest


pytestmark = pytest.mark.asyncio

async def test_images_get(client):
    """Test case for images_get

    Get all Images
    """
    params = [('sort', 'sort_example'),
                    ('type', 'type_example'),
                    ('status', 'status_example'),
                    ('bound_to', 'bound_to_example'),
                    ('include_deprecated', True),
                    ('name', 'name_example'),
                    ('label_selector', 'label_selector_example'),
                    ('architecture', 'architecture_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/images',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_id_delete(client):
    """Test case for images_id_delete

    Delete an Image
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/images/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_id_get(client):
    """Test case for images_id_get

    Get an Image
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/images/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_id_put(client):
    """Test case for images_id_put

    Update an Image
    """
    body = {"description":"My new Image description","type":"snapshot","labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/images/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

