# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_avatars_get_browser(client):
    """Test case for avatars_get_browser

    Get Browser Icon
    """
    params = [('width', 100),
                    ('height', 100),
                    ('quality', 100)]
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/avatars/browsers/{code}'.format(code='code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_avatars_get_credit_card(client):
    """Test case for avatars_get_credit_card

    Get Credit Card Icon
    """
    params = [('width', 100),
                    ('height', 100),
                    ('quality', 100)]
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/avatars/credit-cards/{code}'.format(code='code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_avatars_get_favicon(client):
    """Test case for avatars_get_favicon

    Get Favicon
    """
    params = [('url', 'url_example')]
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/avatars/favicon',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_avatars_get_flag(client):
    """Test case for avatars_get_flag

    Get Country Flag
    """
    params = [('width', 100),
                    ('height', 100),
                    ('quality', 100)]
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/avatars/flags/{code}'.format(code='code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_avatars_get_image(client):
    """Test case for avatars_get_image

    Get Image from URL
    """
    params = [('url', 'url_example'),
                    ('width', 400),
                    ('height', 400)]
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/avatars/image',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_avatars_get_initials(client):
    """Test case for avatars_get_initials

    Get User Initials
    """
    params = [('name', ''),
                    ('width', 500),
                    ('height', 500),
                    ('color', ''),
                    ('background', '')]
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/avatars/initials',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_avatars_get_qr(client):
    """Test case for avatars_get_qr

    Get QR Code
    """
    params = [('text', 'text_example'),
                    ('size', 400),
                    ('margin', 1),
                    ('download', False)]
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/avatars/qr',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

