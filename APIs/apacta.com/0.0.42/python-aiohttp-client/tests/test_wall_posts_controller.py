# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.wall_posts_get200_response import WallPostsGet200Response
from openapi_server.models.wall_posts_post_request import WallPostsPostRequest
from openapi_server.models.wall_posts_wall_post_id_get200_response import WallPostsWallPostIdGet200Response
from openapi_server.models.wall_posts_wall_post_id_wall_comments_get200_response import WallPostsWallPostIdWallCommentsGet200Response


pytestmark = pytest.mark.asyncio

async def test_wall_posts_get(client):
    """Test case for wall_posts_get

    View list of wall posts
    """
    params = [('project_id', 'project_id_example'),
                    ('user_id', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/wall_posts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wall_posts_post(client):
    """Test case for wall_posts_post

    Add a wall post
    """
    body = openapi_server.WallPostsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/wall_posts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wall_posts_wall_post_id_get(client):
    """Test case for wall_posts_wall_post_id_get

    View wall post
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/wall_posts/{wall_post_id}'.format(wall_post_id='wall_post_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wall_posts_wall_post_id_wall_comments_get(client):
    """Test case for wall_posts_wall_post_id_wall_comments_get

    See wall comments to a wall post
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/wall_posts/{wall_post_id}/wall_comments'.format(wall_post_id='wall_post_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

