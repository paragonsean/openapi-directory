# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_translate_cheunh_get(client):
    """Test case for translate_cheunh_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/cheunh',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_gungan_get(client):
    """Test case for translate_gungan_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/gungan',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_huttese_get(client):
    """Test case for translate_huttese_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/huttese',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_mandalorian_get(client):
    """Test case for translate_mandalorian_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/mandalorian',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_sith_get(client):
    """Test case for translate_sith_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/sith',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_yoda_get(client):
    """Test case for translate_yoda_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/yoda',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

