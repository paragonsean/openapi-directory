# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.book import Book


pytestmark = pytest.mark.asyncio

async def test_book_isbn_get(client):
    """Test case for book_isbn_get

    Gets book details
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/book/{isbn}'.format(isbn='isbn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_query_get(client):
    """Test case for books_query_get

    Search books
    """
    params = [('page', 'page_example'),
                    ('author', 'author_example'),
                    ('pageSize', 'page_size_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/{query}'.format(query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

