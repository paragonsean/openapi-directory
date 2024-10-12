# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_tags_to_channel_request import AddTagsToChannelRequest
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.tag import Tag


pytestmark = pytest.mark.asyncio

async def test_add_channel_tag(client):
    """Test case for add_channel_tag

    Add a specific tag to a channel
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.tag+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_id}/tags/{word}'.format(channel_id=927, word='awesome'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_tags_to_channel(client):
    """Test case for add_tags_to_channel

    Add a list of tags to a channel
    """
    body = openapi_server.AddTagsToChannelRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.tag+json',
        'Content-Type': 'application/vnd.vimeo.tag+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_id}/tags'.format(channel_id=927),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_if_channel_has_tag(client):
    """Test case for check_if_channel_has_tag

    Check if a tag has been added to a channel
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.tag+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/tags/{word}'.format(channel_id=927, word='awesome'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tag_from_channel(client):
    """Test case for delete_tag_from_channel

    Remove a tag from a channel
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.tag+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_id}/tags/{word}'.format(channel_id=927, word='awesome'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_tags(client):
    """Test case for get_channel_tags

    Get all the tags that have been added to a channel
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.tag+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/tags'.format(channel_id=927),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

