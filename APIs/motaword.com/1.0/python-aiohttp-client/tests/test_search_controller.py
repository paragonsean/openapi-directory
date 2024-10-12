# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_operation_status import AsyncOperationStatus
from openapi_server.models.search_everywhere_result import SearchEverywhereResult


pytestmark = pytest.mark.asyncio

async def test_check_documents_reindex(client):
    """Test case for check_documents_reindex

    Check reindex status of the client source and translation documents.
    """
    params = [('async_request_key', 'f0db2468-6b77-41a4-bafe-70157bc166ad')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/documents/reindex/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reindex_documents(client):
    """Test case for reindex_documents

    Reindex for search all of the client source and translation documents.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/search/documents/reindex',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_everywhere(client):
    """Test case for search_everywhere

    Search everything in your account
    """
    params = [('query', 'en-US'),
                    ('include[]', ['include_example']),
                    ('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

