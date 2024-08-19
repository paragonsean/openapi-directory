# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_search_response import TflApiPresentationEntitiesSearchResponse


pytestmark = pytest.mark.asyncio

async def test_search_bus_schedules(client):
    """Test case for search_bus_schedules

    Searches the bus schedules folder on S3 for a given bus number.
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Search/BusSchedules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_get(client):
    """Test case for search_get

    Search the site for occurrences of the query string. The maximum number of results returned is equal to the maximum page size              of 100. To return subsequent pages, use the paginated overload.
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_meta_categories(client):
    """Test case for search_meta_categories

    Gets the available search categories.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Search/Meta/Categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_meta_search_providers(client):
    """Test case for search_meta_search_providers

    Gets the available searchProvider names.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Search/Meta/SearchProviders',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_meta_sorts(client):
    """Test case for search_meta_sorts

    Gets the available sorting options.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Search/Meta/Sorts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

