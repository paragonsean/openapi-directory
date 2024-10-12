# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_brotli_get(client):
    """Test case for brotli_get

    Returns Brotli-encoded data.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/brotli',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deflate_get(client):
    """Test case for deflate_get

    Returns Deflate-encoded data.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/deflate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deny_get(client):
    """Test case for deny_get

    Returns page denied by robots.txt rules.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/deny',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_encoding_utf8_get(client):
    """Test case for encoding_utf8_get

    Returns a UTF-8 encoded body.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/encoding/utf8',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gzip_get(client):
    """Test case for gzip_get

    Returns GZip-encoded data.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/gzip',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_html_get(client):
    """Test case for html_get

    Returns a simple HTML document.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/html',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_json_get(client):
    """Test case for json_get

    Returns a simple JSON document.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_robots_txt_get(client):
    """Test case for robots_txt_get

    Returns some robots.txt rules.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/robots.txt',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_xml_get(client):
    """Test case for xml_get

    Returns a simple XML document.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/xml',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

