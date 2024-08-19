# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.image import Image
from openapi_server.models.image_edit import ImageEdit
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_products_id_images_count_json_get(client):
    """Test case for products_id_images_count_json_get

    Count all Product Images.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/images/count.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_images_image_id_json_delete(client):
    """Test case for products_id_images_image_id_json_delete

    Delete a Product Image.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/products/{id}/images/{image_id_jso}'.format(id=56, image_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_images_image_id_json_get(client):
    """Test case for products_id_images_image_id_json_get

    Retrieve a single Product Image.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/images/{image_id_jso}'.format(id=56, image_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_images_json_get(client):
    """Test case for products_id_images_json_get

    Retrieve all Product Images.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/images.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_images_json_post(client):
    """Test case for products_id_images_json_post

    Create a new Product Image.
    """
    body = {"image":{"url":"url"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/products/{id}/images.json'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

