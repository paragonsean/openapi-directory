# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autocomplete_results import AutocompleteResults
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.fda_document_search_results import FDADocumentSearchResults


pytestmark = pytest.mark.asyncio

async def test_autocomplete(client):
    """Test case for autocomplete

    
    """
    params = [('q', 'q_example'),
                    ('page', 1),
                    ('per_page', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/search/autocomplete/{_in}'.format(_in='_in_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_fda_documents(client):
    """Test case for search_fda_documents

    
    """
    params = [('q', 'q_example'),
                    ('text', 'text_example'),
                    ('page', 1),
                    ('per_page', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/search/fda_documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

