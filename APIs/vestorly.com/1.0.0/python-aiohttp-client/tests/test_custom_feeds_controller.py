# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_feed_input import CustomFeedInput
from openapi_server.models.custom_feedresponse import CustomFeedresponse
from openapi_server.models.custom_feeds import CustomFeeds


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_custom_feed(client):
    """Test case for create_custom_feed

    
    """
    custom_feed = openapi_server.CustomFeedInput()
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/custom_feeds',
        headers=headers,
        json=custom_feed,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_custom_feed(client):
    """Test case for delete_custom_feed

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/custom_feeds/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_duplicate_custom_feed(client):
    """Test case for duplicate_custom_feed

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/custom_feeds/{id}/duplicates'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_custom_feed_by_id(client):
    """Test case for find_custom_feed_by_id

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/custom_feeds/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_custom_feeds(client):
    """Test case for find_custom_feeds

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/custom_feeds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_category_by_id(client):
    """Test case for update_category_by_id

    
    """
    custom_feed = openapi_server.CustomFeedInput()
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/custom_feeds/{id}'.format(id='id_example'),
        headers=headers,
        json=custom_feed,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

