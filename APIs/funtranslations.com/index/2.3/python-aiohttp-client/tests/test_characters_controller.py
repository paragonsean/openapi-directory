# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_translate_chef_get(client):
    """Test case for translate_chef_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/chef',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_dolan_get(client):
    """Test case for translate_dolan_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/dolan',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_ferblatin_get(client):
    """Test case for translate_ferblatin_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/ferblatin',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_fudd_get(client):
    """Test case for translate_fudd_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/fudd',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_minion_get(client):
    """Test case for translate_minion_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/minion',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_pirate_get(client):
    """Test case for translate_pirate_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/pirate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

