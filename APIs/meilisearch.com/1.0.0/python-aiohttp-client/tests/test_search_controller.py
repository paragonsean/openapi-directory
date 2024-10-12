# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_in_index1_request import SearchInIndex1Request


pytestmark = pytest.mark.asyncio

async def test_search_in_index(client):
    """Test case for search_in_index

    Search in index
    """
    params = [('q', 'prinec'),
                    ('offset', '0'),
                    ('limit', '1'),
                    ('attributesToRetrieve', 'title,author'),
                    ('attributesToCrop', 'title'),
                    ('attributesToHighlight', '*'),
                    ('cropLength', '5'),
                    ('cropMarker', '[...]'),
                    ('filter', 'genre=\"fantasy\"'),
                    ('showMatchesPosition', 'true'),
                    ('facets', 'genre'),
                    ('sort', 'price'),
                    ('highlightPreTag', '<mark>'),
                    ('highlightPostTag', '</mark>'),
                    ('matchingStrategy', 'all'),
                    ('page', '2'),
                    ('hitsPerPage', '50')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_in_index1(client):
    """Test case for search_in_index1

    Search in index
    """
    body = {"attributesToHighlight":["title"],"q":""}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/indexes/books/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

