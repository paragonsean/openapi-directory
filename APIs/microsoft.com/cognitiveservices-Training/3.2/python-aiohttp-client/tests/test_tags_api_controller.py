# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.tag import Tag


pytestmark = pytest.mark.asyncio

async def test_create_tag(client):
    """Test case for create_tag

    Create a tag for the project.
    """
    params = [('name', 'Tag1'),
                    ('description', 'Description of Tag1'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.2/training/projects/{project_id}/tags'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tag(client):
    """Test case for delete_tag

    Delete a tag from the project.
    """
    headers = { 
        'Accept': '*/*',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/customvision/v3.2/training/projects/{project_id}/tags/{tag_id}'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e', tag_id='9e27bc1b-7ae7-4e3b-a4e5-36153479dc01'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tag(client):
    """Test case for get_tag

    Get information about a specific tag.
    """
    params = [('iterationId', 'iteration_id_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v3.2/training/projects/{project_id}/tags/{tag_id}'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e', tag_id='9e27bc1b-7ae7-4e3b-a4e5-36153479dc01'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tags(client):
    """Test case for get_tags

    Get the tags for a given project and iteration.
    """
    params = [('iterationId', 'iteration_id_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v3.2/training/projects/{project_id}/tags'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_tag(client):
    """Test case for update_tag

    Update a tag.
    """
    body = {"imageCount":0,"name":"name","description":"description","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"Regular"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/customvision/v3.2/training/projects/{project_id}/tags/{tag_id}'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e', tag_id='9e27bc1b-7ae7-4e3b-a4e5-36153479dc01'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

