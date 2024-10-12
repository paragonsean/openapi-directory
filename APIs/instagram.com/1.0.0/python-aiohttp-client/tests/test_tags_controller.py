# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tag_info_response import TagInfoResponse
from openapi_server.models.tag_media_list_response import TagMediaListResponse
from openapi_server.models.tag_search_response import TagSearchResponse


pytestmark = pytest.mark.asyncio

async def test_tags_search_get(client):
    """Test case for tags_search_get

    Search for tags by name.
    """
    params = [('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/tags/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_tag_name_get(client):
    """Test case for tags_tag_name_get

    Get information about a tag object.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/tags/{tag_name}'.format(tag_name='tag_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_tag_name_media_recent_get(client):
    """Test case for tags_tag_name_media_recent_get

    Get a list of recently tagged media.
    """
    params = [('count', 56),
                    ('min_tag_id', 'min_tag_id_example'),
                    ('max_tag_id', 'max_tag_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/tags/{tag_name}/media/recent'.format(tag_name='tag_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

