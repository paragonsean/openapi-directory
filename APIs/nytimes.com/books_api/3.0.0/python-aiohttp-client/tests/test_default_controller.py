# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_lists_best_sellers_history_json200_response import GETListsBestSellersHistoryJson200Response
from openapi_server.models.get_lists_date_list_json200_response import GETListsDateListJson200Response
from openapi_server.models.get_lists_format200_response import GETListsFormat200Response
from openapi_server.models.get_lists_names_format200_response import GETListsNamesFormat200Response
from openapi_server.models.get_lists_overview_format200_response import GETListsOverviewFormat200Response
from openapi_server.models.get_reviews_format200_response import GETReviewsFormat200Response


pytestmark = pytest.mark.asyncio

async def test_g_et_lists_best_sellers_history_json(client):
    """Test case for g_et_lists_best_sellers_history_json

    Best Seller History List
    """
    params = [('age-group', 'age_group_example'),
                    ('author', 'author_example'),
                    ('contributor', 'contributor_example'),
                    ('isbn', 'isbn_example'),
                    ('price', 'price_example'),
                    ('publisher', 'publisher_example'),
                    ('title', 'title_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/books/v3/lists/best-sellers/history.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_lists_date_list_json(client):
    """Test case for g_et_lists_date_list_json

    Best Seller List by Date
    """
    params = [('isbn', 56),
                    ('list-name', 'list_name_example'),
                    ('published-date', '2013-10-20T19:20:30+01:00'),
                    ('bestsellers-date', 'bestsellers_date_example'),
                    ('weeks-on-list', 56),
                    ('rank', 'rank_example'),
                    ('rank-last-week', 56),
                    ('offset', 56),
                    ('sort-order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/books/v3/lists/{_date}/{list_jso}'.format(_date='_date_example', list='list_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_lists_format(client):
    """Test case for g_et_lists_format

    Best Seller List
    """
    params = [('list', 'list_example'),
                    ('weeks-on-list', 56),
                    ('bestsellers-date', '2013-10-20T19:20:30+01:00'),
                    ('date', '_date_example'),
                    ('isbn', 'isbn_example'),
                    ('published-date', 'published_date_example'),
                    ('rank', 56),
                    ('rank-last-week', 56),
                    ('offset', 56),
                    ('sort-order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/books/v3/lists.{format}'.format(format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_lists_names_format(client):
    """Test case for g_et_lists_names_format

    Best Seller List Names
    """
    params = [('api-key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/books/v3/lists/names.{format}'.format(format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_lists_overview_format(client):
    """Test case for g_et_lists_overview_format

    Best Seller List Overview
    """
    params = [('published_date', 'published_date_example'),
                    ('api-key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/books/v3/lists/overview.{format}'.format(format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_reviews_format(client):
    """Test case for g_et_reviews_format

    Reviews
    """
    params = [('isbn', 56),
                    ('title', 'title_example'),
                    ('author', 'author_example'),
                    ('api-key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/books/v3/reviews.{format}'.format(format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

