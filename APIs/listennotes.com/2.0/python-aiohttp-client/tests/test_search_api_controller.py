# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.related_searches_response import RelatedSearchesResponse
from openapi_server.models.search_response import SearchResponse
from openapi_server.models.spell_check_response import SpellCheckResponse
from openapi_server.models.trending_searches_response import TrendingSearchesResponse
from openapi_server.models.typeahead_response import TypeaheadResponse


pytestmark = pytest.mark.asyncio

async def test_get_related_searches(client):
    """Test case for get_related_searches

    Fetch related search terms
    """
    params = [('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/related_searches',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_trending_searches(client):
    """Test case for get_trending_searches

    Fetch trending search terms
    """
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/trending_searches',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Full-text search
    """
    params = [('q', 'q_example'),
                    ('sort_by_date', 0),
                    ('type', episode),
                    ('offset', 0),
                    ('len_min', 0),
                    ('len_max', 56),
                    ('episode_count_min', 56),
                    ('episode_count_max', 56),
                    ('update_freq_min', 56),
                    ('update_freq_max', 56),
                    ('genre_ids', 'genre_ids_example'),
                    ('published_before', 56),
                    ('published_after', 0),
                    ('only_in', 'title,description,author,audio'),
                    ('language', 'language_example'),
                    ('region', 'region_example'),
                    ('ocid', 'ocid_example'),
                    ('ncid', 'ncid_example'),
                    ('safe_mode', 0),
                    ('unique_podcasts', 0),
                    ('page_size', 10)]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spellcheck(client):
    """Test case for spellcheck

    Spell check on a search term
    """
    params = [('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/spellcheck',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_typeahead(client):
    """Test case for typeahead

    Typeahead search
    """
    params = [('q', 'q_example'),
                    ('show_podcasts', 0),
                    ('show_genres', 0),
                    ('safe_mode', 0)]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/typeahead',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

