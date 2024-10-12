# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erskine_may_index_term_search_result_erskine_may_search import ErskineMayIndexTermSearchResultErskineMaySearch
from openapi_server.models.erskine_may_paragraph_search_result_erskine_may_search import ErskineMayParagraphSearchResultErskineMaySearch
from openapi_server.models.erskine_may_section_overview import ErskineMaySectionOverview
from openapi_server.models.erskine_may_section_search_result_erskine_may_search import ErskineMaySectionSearchResultErskineMaySearch


pytestmark = pytest.mark.asyncio

async def test_api_search_index_term_search_results_search_term_get(client):
    """Test case for api_search_index_term_search_results_search_term_get

    Returns a list of index terms which contain the search term.
    """
    params = [('skip', 0),
                    ('take', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Search/IndexTermSearchResults/{search_term}'.format(search_term='search_term_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_search_paragraph_reference_get(client):
    """Test case for api_search_paragraph_reference_get

    Returns a section overview by reference.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Search/Paragraph/{reference}'.format(reference='reference_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_search_paragraph_search_results_search_term_get(client):
    """Test case for api_search_paragraph_search_results_search_term_get

    Returns a list of paragraphs which contain the search term.
    """
    params = [('skip', 0),
                    ('take', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Search/ParagraphSearchResults/{search_term}'.format(search_term='search_term_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_search_section_search_results_search_term_get(client):
    """Test case for api_search_section_search_results_search_term_get

    Returns a list of sections which contain the search term.
    """
    params = [('skip', 0),
                    ('take', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Search/SectionSearchResults/{search_term}'.format(search_term='search_term_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

