# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.organic_result import OrganicResult
from openapi_server.models.scrape_result import ScrapeResult


pytestmark = pytest.mark.asyncio

async def test_search_v1_fields_get(client):
    """Test case for search_v1_fields_get

    
    """
    params = [('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/search/v1/fields',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_v1_organic_get(client):
    """Test case for search_v1_organic_get

    
    """
    params = [('q', 'q_example'),
                    ('field', 'identifier'),
                    ('size', 1000),
                    ('total_only', False),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/search/v1/organic',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_v1_scrape_get(client):
    """Test case for search_v1_scrape_get

    
    """
    params = [('q', 'q_example'),
                    ('field', 'identifier'),
                    ('sort', 'sort_example'),
                    ('size', 1000),
                    ('cursor', 'cursor_example'),
                    ('total_only', False),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/search/v1/scrape',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

