# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.item_clip_files_list import ItemClipFilesList
from openapi_server.models.item_detail import ItemDetail
from openapi_server.models.item_downloadable_list import ItemDownloadableList
from openapi_server.models.item_downloadable_request import ItemDownloadableRequest
from openapi_server.models.item_list import ItemList
from openapi_server.models.item_schedule_list import ItemScheduleList
from openapi_server.models.media_file import MediaFile
from openapi_server.models.next_playback_item import NextPlaybackItem
from openapi_server.models.plan import Plan
from openapi_server.models.search_results import SearchResults
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_get_anon_next_playback_item(client):
    """Test case for get_anon_next_playback_item

    
    """
    params = [('max_rating', 'max_rating_example'),
                    ('expand', 'expand_example'),
                    ('device', 'web_browser'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/items/{item_id}/next'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item(client):
    """Test case for get_item

    
    """
    params = [('max_rating', 'max_rating_example'),
                    ('expand', 'expand_example'),
                    ('select_season', 'select_season_example'),
                    ('use_custom_id', True),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/items/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_children_list(client):
    """Test case for get_item_children_list

    
    """
    params = [('page', 1),
                    ('page_size', 12),
                    ('max_rating', 'max_rating_example'),
                    ('order', desc),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/items/{id}/children'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_downloadables(client):
    """Test case for get_item_downloadables

    
    """
    body = {"ids":"1234,2345,3456"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/items/downloadable',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_related_list(client):
    """Test case for get_item_related_list

    
    """
    params = [('page', 1),
                    ('page_size', 12),
                    ('max_rating', 'max_rating_example'),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/items/{id}/related'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_items_media_clip_files(client):
    """Test case for get_items_media_clip_files

    
    """
    body = {"ids":"1234,2345,3456"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/items/clips',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list(client):
    """Test case for get_list

    
    """
    params = [('page', 1),
                    ('page_size', 12),
                    ('max_rating', 'max_rating_example'),
                    ('order', desc),
                    ('order_by', 'order_by_example'),
                    ('param', 'param_example'),
                    ('item_type', 'item_type_example'),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/lists/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lists(client):
    """Test case for get_lists

    
    """
    params = [('ids', ['ids_example']),
                    ('page_size', 12),
                    ('max_rating', 'max_rating_example'),
                    ('order', desc),
                    ('order_by', 'order_by_example'),
                    ('item_type', 'item_type_example'),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/lists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_item_media_files(client):
    """Test case for get_public_item_media_files

    
    """
    params = [('delivery', ['delivery_example']),
                    ('resolution', 'resolution_example'),
                    ('formats', ['formats_example']),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/items/{id}/videos'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_schedules(client):
    """Test case for get_schedules

    
    """
    params = [('channels', ['channels_example']),
                    ('date', '2013-10-20'),
                    ('hour', 56),
                    ('duration', 56),
                    ('intersect', False),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/schedules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_plans_id_get(client):
    """Test case for plans_id_get

    
    """
    params = [('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/plans/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    
    """
    params = [('term', 'term_example'),
                    ('include', ['include_example']),
                    ('group', True),
                    ('max_results', 20),
                    ('max_rating', 'max_rating_example'),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

