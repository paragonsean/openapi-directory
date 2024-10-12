# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bookmark import Bookmark
from openapi_server.models.item_list import ItemList
from openapi_server.models.next_playback_item import NextPlaybackItem
from openapi_server.models.profile_detail import ProfileDetail
from openapi_server.models.service_error import ServiceError
from openapi_server.models.user_rating import UserRating
from openapi_server.models.watched import Watched


pytestmark = pytest.mark.asyncio

async def test_bookmark_item(client):
    """Test case for bookmark_item

    
    """
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/account/profile/bookmarks/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_item_bookmark(client):
    """Test case for delete_item_bookmark

    
    """
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/account/profile/bookmarks/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_watched(client):
    """Test case for delete_watched

    
    """
    params = [('item_ids', ['item_ids_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/account/profile/watched',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bookmark_list(client):
    """Test case for get_bookmark_list

    
    """
    params = [('page', 56),
                    ('page_size', 56),
                    ('order', desc),
                    ('item_type', 'item_type_example'),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/account/profile/bookmarks/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bookmarks(client):
    """Test case for get_bookmarks

    
    """
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/account/profile/bookmarks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_continue_watching_list(client):
    """Test case for get_continue_watching_list

    
    """
    params = [('show_item_type', episode),
                    ('include', []),
                    ('page', 1),
                    ('page_size', 12),
                    ('max_rating', 'max_rating_example'),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/account/profile/continue-watching/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_bookmark(client):
    """Test case for get_item_bookmark

    
    """
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/account/profile/bookmarks/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_rating(client):
    """Test case for get_item_rating

    
    """
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/account/profile/ratings/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_watched_status(client):
    """Test case for get_item_watched_status

    
    """
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/account/profile/watched/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_next_playback_item(client):
    """Test case for get_next_playback_item

    
    """
    params = [('max_rating', 'max_rating_example'),
                    ('expand', 'expand_example'),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/account/profile/items/{item_id}/next'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile(client):
    """Test case for get_profile

    
    """
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/account/profile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ratings(client):
    """Test case for get_ratings

    
    """
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/account/profile/ratings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ratings_list(client):
    """Test case for get_ratings_list

    
    """
    params = [('page', 1),
                    ('page_size', 12),
                    ('order', desc),
                    ('order_by', date-added),
                    ('item_type', 'item_type_example'),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/account/profile/ratings/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_watched(client):
    """Test case for get_watched

    
    """
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/account/profile/watched',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_watched_list(client):
    """Test case for get_watched_list

    
    """
    params = [('page', 1),
                    ('page_size', 12),
                    ('completed', True),
                    ('order', desc),
                    ('order_by', date-added),
                    ('item_type', 'item_type_example'),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/account/profile/watched/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rate_item(client):
    """Test case for rate_item

    
    """
    params = [('rating', 56),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/account/profile/ratings/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_item_watched_status(client):
    """Test case for set_item_watched_status

    
    """
    params = [('position', 56),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/account/profile/watched/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

