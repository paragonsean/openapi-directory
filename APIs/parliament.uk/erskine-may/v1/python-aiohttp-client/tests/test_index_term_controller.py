# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erskine_may_index_term import ErskineMayIndexTerm
from openapi_server.models.erskine_may_index_term_search_result_erskine_may_search import ErskineMayIndexTermSearchResultErskineMaySearch


pytestmark = pytest.mark.asyncio

async def test_api_index_term_browse_get(client):
    """Test case for api_index_term_browse_get

    Returns a list of index terms by start letter.
    """
    params = [('startLetter', 'start_letter_example'),
                    ('skip', 0),
                    ('take', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/IndexTerm/browse',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_index_term_index_term_id_get(client):
    """Test case for api_index_term_index_term_id_get

    Returns an index term by id.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/IndexTerm/{index_term_id}'.format(index_term_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

