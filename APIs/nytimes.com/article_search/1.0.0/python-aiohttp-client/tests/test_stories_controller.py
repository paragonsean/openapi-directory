# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.articlesearch_json_get200_response import ArticlesearchJsonGet200Response


pytestmark = pytest.mark.asyncio

async def test_articlesearch_json_get(client):
    """Test case for articlesearch_json_get

    Article Search
    """
    params = [('q', 'q_example'),
                    ('fq', 'fq_example'),
                    ('begin_date', 'begin_date_example'),
                    ('end_date', 'end_date_example'),
                    ('sort', 'sort_example'),
                    ('fl', 'fl_example'),
                    ('hl', False),
                    ('page', 0),
                    ('facet_field', 'facet_field_example'),
                    ('facet_filter', False)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/search/v2/articlesearch.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

