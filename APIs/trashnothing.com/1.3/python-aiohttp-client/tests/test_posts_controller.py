# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_all_posts200_response import GetAllPosts200Response
from openapi_server.models.get_all_posts_changes200_response import GetAllPostsChanges200Response
from openapi_server.models.get_post_and_related_data200_response import GetPostAndRelatedData200Response
from openapi_server.models.get_posts200_response import GetPosts200Response
from openapi_server.models.get_posts_by_ids200_response import GetPostsByIds200Response
from openapi_server.models.post import Post
from openapi_server.models.search_posts200_response import SearchPosts200Response


pytestmark = pytest.mark.asyncio

async def test_get_all_posts(client):
    """Test case for get_all_posts

    List all posts
    """
    params = [('types', 'types_example'),
                    ('date_min', '2013-10-20T19:20:30+01:00'),
                    ('date_max', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 20),
                    ('page', 1),
                    ('device_pixel_ratio', 1)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.3/posts/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_posts_changes(client):
    """Test case for get_all_posts_changes

    List all post changes
    """
    params = [('date_min', '2013-10-20T19:20:30+01:00'),
                    ('date_max', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 20),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.3/posts/all/changes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_post(client):
    """Test case for get_post

    Retrieve a post
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.3/posts/{post_id}'.format(post_id='post_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_post_and_related_data(client):
    """Test case for get_post_and_related_data

    Retrieve post display data
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.3/posts/{post_id}/display'.format(post_id='post_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_posts(client):
    """Test case for get_posts

    List posts
    """
    params = [('sort_by', 'date'),
                    ('types', 'types_example'),
                    ('sources', 'sources_example'),
                    ('group_ids', 'The group IDs of every group the current user is a member of.'),
                    ('per_page', 20),
                    ('page', 1),
                    ('device_pixel_ratio', 1),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 3.4),
                    ('date_min', '2013-10-20T19:20:30+01:00'),
                    ('date_max', '2013-10-20T19:20:30+01:00'),
                    ('outcomes', ''),
                    ('user_state', ''),
                    ('include_reposts', 1)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.3/posts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_posts_by_ids(client):
    """Test case for get_posts_by_ids

    Retrieve multiple posts
    """
    params = [('post_ids', 'post_ids_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.3/posts/multiple',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_posts(client):
    """Test case for search_posts

    Search posts
    """
    params = [('search', 'search_example'),
                    ('sort_by', 'relevance'),
                    ('types', 'types_example'),
                    ('sources', 'sources_example'),
                    ('group_ids', 'The group IDs of every group the current user is a member of.'),
                    ('per_page', 20),
                    ('page', 1),
                    ('device_pixel_ratio', 1),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 3.4),
                    ('date_min', '2013-10-20T19:20:30+01:00'),
                    ('date_max', '2013-10-20T19:20:30+01:00'),
                    ('outcomes', ''),
                    ('user_state', ''),
                    ('include_reposts', 1)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.3/posts/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

