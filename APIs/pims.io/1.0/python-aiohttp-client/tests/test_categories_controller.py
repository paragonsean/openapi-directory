# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.categories_entity import CategoriesEntity
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.events_categories_entity import EventsCategoriesEntity


pytestmark = pytest.mark.asyncio

async def test_fetch_all_categories(client):
    """Test case for fetch_all_categories

    Find all categories
    """
    params = [('label', 'label_example'),
                    ('show_ignored', False),
                    ('sort', order),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_all_events_categories(client):
    """Test case for fetch_all_events_categories

    Find all categories for one event
    """
    params = [('show_ignored', False),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}/categories'.format(event_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_one_category(client):
    """Test case for fetch_one_category

    Get one category by ID
    """
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/categories/{category_id}'.format(category_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_one_event_category(client):
    """Test case for fetch_one_event_category

    Get one event category by ID
    """
    params = [('show_ignored', False)]
    headers = { 
        'Accept': 'application/hal+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}/categories/{category_id}'.format(event_id=56, category_id=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

