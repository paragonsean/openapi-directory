# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.category import Category
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.suggest_video_category_request import SuggestVideoCategoryRequest
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_check_category_for_video(client):
    """Test case for check_category_for_video

    Check for a video in a category
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/categories/{category}/videos/{video_id}'.format(category='animation', video_id=273576296),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_category_videos(client):
    """Test case for get_category_videos

    Get all the videos in a category
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('filter_embeddable', true),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/categories/{category}/videos'.format(category='animation'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_categories(client):
    """Test case for get_video_categories

    Get all the categories to which a video belongs
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.category+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/categories'.format(video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suggest_video_category(client):
    """Test case for suggest_video_category

    Suggest categories for a video
    """
    body = openapi_server.SuggestVideoCategoryRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.category+json',
        'Content-Type': 'application/vnd.vimeo.category+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/videos/{video_id}/categories'.format(video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

