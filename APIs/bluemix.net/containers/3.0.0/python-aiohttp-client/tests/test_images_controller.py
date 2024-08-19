# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.image_detail import ImageDetail
from openapi_server.models.image_info import ImageInfo


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/tar not supported by Connexion")
async def test_build_post(client):
    """Test case for build_post

    Build a Docker image from a Dockerfile
    """
    body = '/path/to/file'
    params = [('t', 't_example'),
                    ('q', True),
                    ('nocache', True),
                    ('pull', True)]
    headers = { 
        'Content-Type': 'application/tar',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/build',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_id_delete(client):
    """Test case for images_id_delete

    Remove a Docker image.
    """
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/images/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_json_get(client):
    """Test case for images_json_get

    List all Docker images that are available in your private Bluemix registry.
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/images/json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_name_or_id_json_get(client):
    """Test case for images_name_or_id_json_get

    Inspect a Docker image in private Bluemix registry
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/images/{name_or_id}/json'.format(name_or_id='name_or_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

