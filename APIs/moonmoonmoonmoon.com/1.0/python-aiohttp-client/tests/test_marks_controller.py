# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_marks_hashtags(client):
    """Test case for marks_hashtags

    Fetches popular hashtags or marks tagged with specified hashtag
    """
    params = [('tag', 'tag_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/hashtags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marks_index(client):
    """Test case for marks_index

    Fetches marks
    """
    params = [('before', 'before_example'),
                    ('popular', True),
                    ('last_popular_id', 'last_popular_id_example'),
                    ('featured', True),
                    ('x', 56),
                    ('y', 56),
                    ('user', 'user_example'),
                    ('collection', 'collection_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/marks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

