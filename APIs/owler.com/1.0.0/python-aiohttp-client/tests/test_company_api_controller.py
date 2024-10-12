# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.basic_results import BasicResults
from openapi_server.models.company import Company
from openapi_server.models.results import Results


pytestmark = pytest.mark.asyncio

async def test_basic_company_search(client):
    """Test case for basic_company_search

    Basic Search Company by Ticker or Website or Name or PermID
    """
    params = [('q', 'q_example'),
                    ('fields', ['fields_example']),
                    ('limit', 'limit_example'),
                    ('format', json)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/basicsearch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fuzzy_company_search(client):
    """Test case for fuzzy_company_search

    Fuzzy Search Company by Name or Address or Phone
    """
    params = [('q', 'q_example'),
                    ('fields', ['fields_example']),
                    ('limit', 'limit_example'),
                    ('format', json)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/fuzzysearch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_company(client):
    """Test case for search_company

    Search Company by Ticker or Website or Name or PermID
    """
    params = [('q', 'q_example'),
                    ('fields', ['fields_example']),
                    ('limit', 'limit_example'),
                    ('format', json)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_company_id_company_id_get(client):
    """Test case for v1_company_id_company_id_get

    Get Company by Id
    """
    params = [('format', json)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/id/{company_id}'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_company_url_website_get(client):
    """Test case for v1_company_url_website_get

    Get Company by URL
    """
    params = [('format', json)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/url/{website}'.format(website='website_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

