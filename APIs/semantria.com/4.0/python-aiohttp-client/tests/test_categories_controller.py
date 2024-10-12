# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.category_response_version import CategoryResponseVersion


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_add_categories(client):
    """Test case for add_categories

    Add user categories
    """
    categories = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/categories.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=categories,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_categories(client):
    """Test case for delete_categories

    Remove user categories
    """
    category_ids = ['category_ids_example']
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/categories.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=category_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_categories(client):
    """Test case for get_categories

    Retrieve user categories
    """
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/categories.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_categories(client):
    """Test case for update_categories

    Updates user categories
    """
    categories = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/categories.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=categories,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

