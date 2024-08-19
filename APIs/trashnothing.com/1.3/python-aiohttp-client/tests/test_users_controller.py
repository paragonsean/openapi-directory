# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_posts200_response import GetPosts200Response
from openapi_server.models.search_posts200_response import SearchPosts200Response


pytestmark = pytest.mark.asyncio

async def test_get_user_posts(client):
    """Test case for get_user_posts

    List posts by a user
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
                    ('include_reposts', 1)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.3/users/{user_id}/posts'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_user_posts(client):
    """Test case for search_user_posts

    Search posts by a user
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
                    ('include_reposts', 1)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.3/users/{user_id}/posts/search'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

