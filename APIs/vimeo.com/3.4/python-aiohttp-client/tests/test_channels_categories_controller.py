# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_channel_categories_request import AddChannelCategoriesRequest
from openapi_server.models.category import Category
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError


pytestmark = pytest.mark.asyncio

async def test_add_channel_categories(client):
    """Test case for add_channel_categories

    Add a list of categories to a channel
    """
    body = openapi_server.AddChannelCategoriesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_id}/categories'.format(channel_id=927),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categorize_channel(client):
    """Test case for categorize_channel

    Categorize a channel
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.category+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_id}/categories/{category}'.format(category='animation', channel_id=927),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel_category(client):
    """Test case for delete_channel_category

    Remove a category from a channel
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.category+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_id}/categories/{category}'.format(category='animation', channel_id=927),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_categories(client):
    """Test case for get_channel_categories

    Get all the categories in a channel
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.category+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/categories'.format(channel_id=927),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

