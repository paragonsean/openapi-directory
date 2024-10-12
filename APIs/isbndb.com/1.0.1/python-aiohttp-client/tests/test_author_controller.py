# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.author import Author
from openapi_server.models.author_query_results import AuthorQueryResults


pytestmark = pytest.mark.asyncio

async def test_author_name_get(client):
    """Test case for author_name_get

    Gets author details
    """
    params = [('page', 'page_example'),
                    ('pageSize', 'page_size_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/author/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authors_query_get(client):
    """Test case for authors_query_get

    Search authors
    """
    params = [('pageSize', 'page_size_example'),
                    ('page', 'page_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/authors/{query}'.format(query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

