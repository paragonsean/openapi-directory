# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_cache_get(client):
    """Test case for cache_get

    Returns a 304 if an If-Modified-Since header or If-None-Match is present. Returns the same as a GET otherwise.
    """
    headers = { 
        'if_modified_since': 'if_modified_since_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/cache',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cache_value_get(client):
    """Test case for cache_value_get

    Sets a Cache-Control header for n seconds.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/cache/{value}'.format(value=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_etag_etag_get(client):
    """Test case for etag_etag_get

    Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.
    """
    headers = { 
        'if_none_match': 'if_none_match_example',
        'if_match': 'if_match_example',
    }
    response = await client.request(
        method='GET',
        path='/etag/{etag}'.format(etag='etag_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_response_headers_get(client):
    """Test case for response_headers_get

    Returns a set of response headers from the query string.
    """
    params = [('freeform', {'key': 'freeform_example'})]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/response-headers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_response_headers_post(client):
    """Test case for response_headers_post

    Returns a set of response headers from the query string.
    """
    params = [('freeform', {'key': 'freeform_example'})]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/response-headers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

