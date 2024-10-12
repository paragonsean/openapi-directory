# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.site import Site
from openapi_server.models.tag import Tag


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_tags(client):
    """Test case for create_tags

    Create a tag
    """
    body = openapi_server.Tag()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/tags',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sites_by_tags(client):
    """Test case for get_sites_by_tags

    Find sites by tag ID
    """
    params = [('name', 'name_example'),
                    ('access_url', 'access_url_example'),
                    ('j_version', 'j_version_example'),
                    ('ip', 'ip_example'),
                    ('jUpdate', 56),
                    ('published', 56),
                    ('error', 'error_example'),
                    ('nbUpdates', 'nb_updates_example'),
                    ('up', 56),
                    ('fields', 'fields_example'),
                    ('limit', 56),
                    ('limitstart', 56),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/tags/{id}/sites'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tag_by_id(client):
    """Test case for get_tag_by_id

    Find tag by ID
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/tags/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_get(client):
    """Test case for tags_get

    Get a list of tags
    """
    params = [('name', 'name_example'),
                    ('type', 'type_example'),
                    ('fields', 'fields_example'),
                    ('limit', 56),
                    ('limitstart', 56),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_id_delete(client):
    """Test case for tags_id_delete

    Delete a specific tag
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/tags/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_metadata_get(client):
    """Test case for tags_metadata_get

    Get the list of fields
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/tags/metadata',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_tag(client):
    """Test case for update_tag

    Update a tag
    """
    body = openapi_server.Tag()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/tags/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

