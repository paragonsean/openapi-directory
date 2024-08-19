# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_tag_response_body import CreateTagResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.list_tags_response_body import ListTagsResponseBody


pytestmark = pytest.mark.asyncio

async def test_create_tag(client):
    """Test case for create_tag

    Create a New Tag
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/tags/{tag_name}'.format(tag_name='tag_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tag(client):
    """Test case for delete_tag

    Delete Tag
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/tags/{tag_name}'.format(tag_name='tag_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags(client):
    """Test case for list_tags

    Get Tags
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/tags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rename_tag(client):
    """Test case for rename_tag

    Update Tag Name
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/tags/{tag_name}/{new_tag_name}'.format(tag_name='tag_name_example', new_tag_name='new_tag_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

