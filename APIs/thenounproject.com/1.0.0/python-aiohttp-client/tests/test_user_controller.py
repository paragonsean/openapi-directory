# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_user_collection(client):
    """Test case for get_user_collection

    Get user collection
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/user/{user_id}/collections/{slug}'.format(user_id=56, slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_collections(client):
    """Test case for get_user_collections

    Get user collections
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/user/{user_id}/collections'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_uploads_with_user(client):
    """Test case for get_user_uploads_with_user

    Get user uploads with user
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('page', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/user/{username}/uploads'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

