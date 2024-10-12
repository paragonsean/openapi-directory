# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.category import Category
from openapi_server.models.legacy_error import LegacyError


pytestmark = pytest.mark.asyncio

async def test_get_categories(client):
    """Test case for get_categories

    Get all categories
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.category+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_category(client):
    """Test case for get_category

    Get a specific category
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.category+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/categories/{category}'.format(category='animation'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

