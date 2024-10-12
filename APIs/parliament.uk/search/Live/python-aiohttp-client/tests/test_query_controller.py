# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_query_extension_get(client):
    """Test case for query_extension_get

    Search results
    """
    params = [('q', 'q_example'),
                    ('start', 3.4),
                    ('count', 3.4),
                    ('subdomains', 'subdomains_example'),
                    ('inUrlPrefixes', 'in_url_prefixes_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/search/query.{extension}'.format(extension='extension_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_get(client):
    """Test case for query_get

    Search results
    """
    params = [('q', 'q_example'),
                    ('start', 3.4),
                    ('count', 3.4),
                    ('subdomains', 'subdomains_example'),
                    ('inUrlPrefixes', 'in_url_prefixes_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/search/query',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

