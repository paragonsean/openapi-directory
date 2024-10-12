# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tag_single import TagSingle
from openapi_server.models.tags_list200_response import TagsList200Response


pytestmark = pytest.mark.asyncio

async def test_tags_list(client):
    """Test case for tags_list

    Get a list of tags.
    """
    params = [('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_read(client):
    """Test case for tags_read

    Get details of the tag.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/tags/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

