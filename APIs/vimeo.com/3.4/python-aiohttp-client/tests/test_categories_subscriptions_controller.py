# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.category import Category
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_check_if_user_subscribed_to_category(client):
    """Test case for check_if_user_subscribed_to_category

    Check if a user follows a category
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/categories/{category}'.format(category='animation', user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_if_user_subscribed_to_category_alt1(client):
    """Test case for check_if_user_subscribed_to_category_alt1

    Check if a user follows a category
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/categories/{category}'.format(category='animation'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_category_subscriptions(client):
    """Test case for get_category_subscriptions

    Get all the categories that a user follows
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
        path='/users/{user_id}/categories'.format(user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_category_subscriptions_alt1(client):
    """Test case for get_category_subscriptions_alt1

    Get all the categories that a user follows
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
        path='/me/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe_to_category(client):
    """Test case for subscribe_to_category

    Subscribe a user to a single category
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{user_id}/categories/{category}'.format(category=0, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe_to_category_alt1(client):
    """Test case for subscribe_to_category_alt1

    Subscribe a user to a single category
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/me/categories/{category}'.format(category=0),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unsubscribe_from_category(client):
    """Test case for unsubscribe_from_category

    Unsubscribe a user from a category
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}/categories/{category}'.format(category='animation', user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unsubscribe_from_category_alt1(client):
    """Test case for unsubscribe_from_category_alt1

    Unsubscribe a user from a category
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/me/categories/{category}'.format(category='animation'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

