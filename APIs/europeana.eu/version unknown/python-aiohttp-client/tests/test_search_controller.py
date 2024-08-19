# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.model_and_view import ModelAndView
from openapi_server.models.search_request import SearchRequest


pytestmark = pytest.mark.asyncio

async def test_open_search(client):
    """Test case for open_search

    basic search function following the OpenSearch specification
    """
    params = [('count', 12),
                    ('searchTerms', 'search_terms_example'),
                    ('startIndex', 1)]
    headers = { 
        'Accept': 'application/xhtml+xml',
    }
    response = await client.request(
        method='GET',
        path='/record/v2/opensearch.rss',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_records(client):
    """Test case for search_records

    search for records
    """
    params = [('boost', 'boost_example'),
                    ('callback', 'param_callback_example'),
                    ('colourpalette', ['colourpalette_example']),
                    ('cursor', 'cursor_example'),
                    ('facet', ['facet_example']),
                    ('hit.fl', 'hit_fl_example'),
                    ('hit.selectors', 'hit_selectors_example'),
                    ('landingpage', True),
                    ('lang', 'lang_example'),
                    ('media', True),
                    ('profile', 'standard'),
                    ('q.source', 'q_source_example'),
                    ('q.target', 'q_target_example'),
                    ('qf', ['qf_example']),
                    ('query', 'query_example'),
                    ('reusability', ['reusability_example']),
                    ('rows', 12),
                    ('sort', 'sort_example'),
                    ('start', 1),
                    ('text_fulltext', True),
                    ('theme', 'theme_example'),
                    ('thumbnail', True),
                    ('wskey', 'wskey_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/record/v2/search.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_records_post(client):
    """Test case for search_records_post

    search for records post
    """
    search_request = {"cursor":"cursor","thumbnail":True,"colourPalette":["colourPalette","colourPalette"],"landingPage":True,"profile":["profile","profile"],"query":"query","start":6,"reusability":["reusability","reusability"],"media":True,"sort":["sort","sort"],"rows":0,"textFulltext":True,"hit":{"fl":"fl","selectors":"selectors"},"qf":["qf","qf"],"callback":"callback","boost":"boost","theme":"theme","facet":["facet","facet"]}
    params = [('wskey', 'wskey_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/record/v2/search.json',
        headers=headers,
        json=search_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_query_using_get(client):
    """Test case for translate_query_using_get

    translate a term to different languages
    """
    params = [('callback', 'param_callback_example'),
                    ('languageCodes', ['language_codes_example']),
                    ('profile', 'profile_example'),
                    ('term', 'term_example'),
                    ('wskey', 'wskey_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/record/v2/translateQuery.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

