# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_feed_request import CreateFeedRequest
from openapi_server.models.feed import Feed
from openapi_server.models.group import Group


pytestmark = pytest.mark.asyncio

async def test_add_feed_to_group_0(client):
    """Test case for add_feed_to_group_0

    Add an existing Feed to a Group
    """
    params = [('feed_key', 'feed_key_example')]
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/groups/{group_key}/add'.format(group_key='group_key_example', username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_feeds(client):
    """Test case for all_feeds

    All feeds for current user
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/feeds'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_group_feeds_0(client):
    """Test case for all_group_feeds_0

    All feeds for current user in a given group
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/groups/{group_key}/feeds'.format(group_key='group_key_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_feed(client):
    """Test case for create_feed

    Create a new Feed
    """
    feed = openapi_server.CreateFeedRequest()
    params = [('group_key', 'group_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/feeds'.format(username='username_example'),
        headers=headers,
        json=feed,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_group_feed(client):
    """Test case for create_group_feed

    Create a new Feed in a Group
    """
    feed = openapi_server.CreateFeedRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/groups/{group_key}/feeds'.format(username='username_example', group_key='group_key_example'),
        headers=headers,
        json=feed,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destroy_feed(client):
    """Test case for destroy_feed

    Delete an existing Feed
    """
    headers = { 
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/{username}/feeds/{feed_key}'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_feed(client):
    """Test case for get_feed

    Get feed by feed key
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/feeds/{feed_key}'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_feed_details(client):
    """Test case for get_feed_details

    Get detailed feed by feed key
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/feeds/{feed_key}/details'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_feed_from_group_0(client):
    """Test case for remove_feed_from_group_0

    Remove a Feed from a Group
    """
    params = [('feed_key', 'feed_key_example')]
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/groups/{group_key}/remove'.format(group_key='group_key_example', username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_replace_feed(client):
    """Test case for replace_feed

    Replace an existing Feed
    """
    feed = openapi_server.CreateFeedRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/{username}/feeds/{feed_key}'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        json=feed,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_feed(client):
    """Test case for update_feed

    Update properties of an existing Feed
    """
    feed = openapi_server.CreateFeedRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/{username}/feeds/{feed_key}'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        json=feed,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

