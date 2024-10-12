# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.combined_result import CombinedResult


pytestmark = pytest.mark.asyncio

async def test_get_omdb_search(client):
    """Test case for get_omdb_search

    OMDb Search
    """
    params = [('t', 't_example'),
                    ('i', 'i_example'),
                    ('s', 's_example'),
                    ('y', 56),
                    ('type', 'type_example'),
                    ('plot', short),
                    ('tomatoes', False),
                    ('r', json),
                    ('v', 1),
                    ('page', 1),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

