# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_all_list_comments(client):
    """Test case for get_all_list_comments

    Get all list comments
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/lists/{id}/comments/{sort}'.format(id=55, sort='newest'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_users_who_liked_a_list(client):
    """Test case for get_all_users_who_liked_a_list

    Get all users who liked a list
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/lists/{id}/likes'.format(id='55'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_items_on_a_list(client):
    """Test case for get_items_on_a_list

    Get items on a list
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/lists/{id}/items/{type}'.format(id='55', type='movies'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list(client):
    """Test case for get_list

    Get list
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/lists/{id}'.format(id=55),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_popular_lists(client):
    """Test case for get_popular_lists

    Get popular lists
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/lists/popular',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_trending_lists(client):
    """Test case for get_trending_lists

    Get trending lists
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/lists/trending',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

