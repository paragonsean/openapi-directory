# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_project_creation_write import UserProjectCreationWrite
from openapi_server.models.user_project_read import UserProjectRead
from openapi_server.models.user_project_write import UserProjectWrite


pytestmark = pytest.mark.asyncio

async def test_delete_user_project_item(client):
    """Test case for delete_user_project_item

    Removes the UserProject resource.
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/user-projects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_project_item(client):
    """Test case for get_user_project_item

    Retrieves a UserProject resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/user-projects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_user_project_collection(client):
    """Test case for post_user_project_collection

    Creates a UserProject resource.
    """
    user_project = openapi_server.UserProjectCreationWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/user-projects',
        headers=headers,
        json=user_project,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_user_project_item(client):
    """Test case for put_user_project_item

    Replaces the UserProject resource.
    """
    user_project = openapi_server.UserProjectWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/user-projects/{id}'.format(id='id_example'),
        headers=headers,
        json=user_project,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

