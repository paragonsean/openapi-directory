# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.qod_response import QODResponse


pytestmark = pytest.mark.asyncio

async def test_qod_categories_get(client):
    """Test case for qod_categories_get

    
    """
    params = [('language', 'en'),
                    ('detailed', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/qod/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_qod_get(client):
    """Test case for qod_get

    
    """
    params = [('category', 'category_example'),
                    ('language', 'en'),
                    ('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/qod',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_qod_languages_get(client):
    """Test case for qod_languages_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/qod/languages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

