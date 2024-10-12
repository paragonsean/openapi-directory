# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_riddle_delete(client):
    """Test case for riddle_delete

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/riddle',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_riddle_get(client):
    """Test case for riddle_get

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/riddle',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_riddle_post(client):
    """Test case for riddle_post

    
    """
    params = [('question', 'question_example'),
                    ('category', 'category_example'),
                    ('answer', 'answer_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/riddle',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_riddle_put(client):
    """Test case for riddle_put

    
    """
    params = [('question', 'question_example'),
                    ('category', 'category_example'),
                    ('answer', 'answer_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/riddle',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

