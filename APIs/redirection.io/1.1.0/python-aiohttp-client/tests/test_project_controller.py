# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.project_creation_write import ProjectCreationWrite
from openapi_server.models.project_list import ProjectList
from openapi_server.models.project_read import ProjectRead
from openapi_server.models.project_write import ProjectWrite


pytestmark = pytest.mark.asyncio

async def test_delete_project_item(client):
    """Test case for delete_project_item

    Removes the Project resource.
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/projects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_collection(client):
    """Test case for get_project_collection

    Retrieves the collection of Project resources.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_item(client):
    """Test case for get_project_item

    Retrieves a Project resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_project_collection(client):
    """Test case for post_project_collection

    Creates a Project resource.
    """
    project = openapi_server.ProjectCreationWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects',
        headers=headers,
        json=project,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_project_item(client):
    """Test case for put_project_item

    Replaces the Project resource.
    """
    project = openapi_server.ProjectWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/projects/{id}'.format(id='id_example'),
        headers=headers,
        json=project,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

