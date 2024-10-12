# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_image_get(client):
    """Test case for image_get

    Returns a simple image of the type suggest by the Accept header.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/image',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_image_jpeg_get(client):
    """Test case for image_jpeg_get

    Returns a simple JPEG image.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/image/jpeg',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_image_png_get(client):
    """Test case for image_png_get

    Returns a simple PNG image.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/image/png',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_image_svg_get(client):
    """Test case for image_svg_get

    Returns a simple SVG image.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/image/svg',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_image_webp_get(client):
    """Test case for image_webp_get

    Returns a simple WEBP image.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/image/webp',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

