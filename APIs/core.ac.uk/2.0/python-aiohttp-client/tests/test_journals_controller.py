# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.journal_response import JournalResponse
from openapi_server.models.journal_search_response import JournalSearchResponse
from openapi_server.models.search_request import SearchRequest


pytestmark = pytest.mark.asyncio

async def test_get_journal_by_issn(client):
    """Test case for get_journal_by_issn

    Find journal by ISSN
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api-v2/journals/get/{issn}'.format(issn='issn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_journal_by_issn_batch(client):
    """Test case for get_journal_by_issn_batch

    Batch operation for retrieving journals by ISSN
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api-v2/journals/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_journals_search_post(client):
    """Test case for journals_search_post

    Batch operation for search through journals
    """
    body = [openapi_server.SearchRequest()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api-v2/journals/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_journals_search_query_get(client):
    """Test case for journals_search_query_get

    Search through journals
    """
    params = [('page', 1),
                    ('pageSize', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api-v2/journals/search/{query}'.format(query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

