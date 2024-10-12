# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_result import SearchResult


pytestmark = pytest.mark.asyncio

async def test_get_matching_observation(client):
    """Test case for get_matching_observation

    Find observation matching given phrase
    """
    params = [('phrase', 'phrase_example'),
                    ('sex', 'sex_example'),
                    ('age.value', 18),
                    ('age.unit', year)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/lookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

