# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_result import SearchResult


pytestmark = pytest.mark.asyncio

async def test_get_matching_observations(client):
    """Test case for get_matching_observations

    Find observations matching given phrase
    """
    params = [('phrase', 'phrase_example'),
                    ('sex', 'sex_example'),
                    ('age.value', 18),
                    ('age.unit', year),
                    ('max_results', 8),
                    ('type', ['type_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

