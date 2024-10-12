# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_organization_creation_write import UserOrganizationCreationWrite
from openapi_server.models.user_organization_read import UserOrganizationRead
from openapi_server.models.user_organization_write import UserOrganizationWrite


pytestmark = pytest.mark.asyncio

async def test_delete_user_organization_item(client):
    """Test case for delete_user_organization_item

    Removes the UserOrganization resource.
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/user-organizations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_organization_item(client):
    """Test case for get_user_organization_item

    Retrieves a UserOrganization resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/user-organizations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_user_organization_collection(client):
    """Test case for post_user_organization_collection

    Creates a UserOrganization resource.
    """
    user_organization = openapi_server.UserOrganizationCreationWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/user-organizations',
        headers=headers,
        json=user_organization,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_user_organization_item(client):
    """Test case for put_user_organization_item

    Replaces the UserOrganization resource.
    """
    user_organization = openapi_server.UserOrganizationWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/user-organizations/{id}'.format(id='id_example'),
        headers=headers,
        json=user_organization,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

