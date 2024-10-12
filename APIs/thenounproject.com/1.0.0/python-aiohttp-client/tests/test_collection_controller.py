# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_collection_by_id(client):
    """Test case for get_collection_by_id

    Get collection by id
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/collection/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_collection_by_slug(client):
    """Test case for get_collection_by_slug

    Get collection by slug
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/collection/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_collection_icons_by_id(client):
    """Test case for get_collection_icons_by_id

    Get collection icons by id
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('page', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/collection/{id}/icons'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_collection_icons_by_slug(client):
    """Test case for get_collection_icons_by_slug

    Get collection icons by slug
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('page', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/collection/{slug}/icons'.format(slug='slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

