# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.organization_read import OrganizationRead
from openapi_server.models.organization_write import OrganizationWrite


pytestmark = pytest.mark.asyncio

async def test_delete_organization_item(client):
    """Test case for delete_organization_item

    Removes the Organization resource.
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/organizations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_item(client):
    """Test case for get_organization_item

    Retrieves a Organization resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_organization_collection(client):
    """Test case for post_organization_collection

    Creates a Organization resource.
    """
    organization = openapi_server.OrganizationWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/organizations',
        headers=headers,
        json=organization,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_organization_item(client):
    """Test case for put_organization_item

    Replaces the Organization resource.
    """
    organization = openapi_server.OrganizationWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/organizations/{id}'.format(id='id_example'),
        headers=headers,
        json=organization,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

