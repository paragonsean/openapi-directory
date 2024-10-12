# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.project_entity import ProjectEntity


pytestmark = pytest.mark.asyncio

async def test_delete_projects_id(client):
    """Test case for delete_projects_id

    Delete Project
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/projects/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_projects(client):
    """Test case for get_projects

    List Projects
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_projects_id(client):
    """Test case for get_projects_id

    Show Project
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/projects/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_projects_id(client):
    """Test case for patch_projects_id

    Update Project
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('global_access', 'global_access_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/projects/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_projects(client):
    """Test case for post_projects

    Create Project
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('global_access', 'global_access_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/projects',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

