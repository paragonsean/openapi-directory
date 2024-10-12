# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.clickwrap_entity import ClickwrapEntity


pytestmark = pytest.mark.asyncio

async def test_delete_clickwraps_id(client):
    """Test case for delete_clickwraps_id

    Delete Clickwrap
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/clickwraps/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_clickwraps(client):
    """Test case for get_clickwraps

    List Clickwraps
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/clickwraps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_clickwraps_id(client):
    """Test case for get_clickwraps_id

    Show Clickwrap
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/clickwraps/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_clickwraps_id(client):
    """Test case for patch_clickwraps_id

    Update Clickwrap
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('body', 'body_example')
    data.add_field('name', 'name_example')
    data.add_field('use_with_bundles', 'use_with_bundles_example')
    data.add_field('use_with_inboxes', 'use_with_inboxes_example')
    data.add_field('use_with_users', 'use_with_users_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/clickwraps/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_clickwraps(client):
    """Test case for post_clickwraps

    Create Clickwrap
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('body', 'body_example')
    data.add_field('name', 'name_example')
    data.add_field('use_with_bundles', 'use_with_bundles_example')
    data.add_field('use_with_inboxes', 'use_with_inboxes_example')
    data.add_field('use_with_users', 'use_with_users_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/clickwraps',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

