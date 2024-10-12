# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fulltext_results_dto import FulltextResultsDto


pytestmark = pytest.mark.asyncio

async def test_fulltxtsearch(client):
    """Test case for fulltxtsearch

    search for places by text around a GPS point
    """
    params = [('q', 'q_example'),
                    ('allwordsrequired', False),
                    ('spellchecking', 'spellchecking_example'),
                    ('lat', 3.4),
                    ('lng', 3.4),
                    ('radius', 10000.0),
                    ('suggest', False),
                    ('style', MEDIUM),
                    ('country', 'country_example'),
                    ('lang', 'lang_example'),
                    ('format', XML),
                    ('from', 1),
                    ('to', 10),
                    ('callback', 'param_callback_example'),
                    ('indent', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/fulltext/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

