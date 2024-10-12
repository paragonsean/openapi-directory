# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_translate_braille_dots_get(client):
    """Test case for translate_braille_dots_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/braille/dots',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_braille_get(client):
    """Test case for translate_braille_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/braille',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_braille_html_get(client):
    """Test case for translate_braille_html_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/braille/html',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_braille_image_get(client):
    """Test case for translate_braille_image_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/braille/image',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_braille_unicode_get(client):
    """Test case for translate_braille_unicode_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/braille/unicode',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

