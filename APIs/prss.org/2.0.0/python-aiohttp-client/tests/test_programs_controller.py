# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.program import Program


pytestmark = pytest.mark.asyncio

async def test_api_v2_programs_id_get(client):
    """Test case for api_v2_programs_id_get

    Returns the program matching the given ID.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/programs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_programs_search_get(client):
    """Test case for api_v2_programs_search_get

    Optimized free-text search for programs using various filters.
    """
    params = [('keywords', 'keywords_example'),
                    ('pageStart', 0),
                    ('pageSize', 500)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/programs/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

