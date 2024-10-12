# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.qod_response import QODResponse
from openapi_server.models.quote_response import QuoteResponse
from openapi_server.models.success_response import SuccessResponse


pytestmark = pytest.mark.asyncio

async def test_qod_get_0(client):
    """Test case for qod_get_0

    
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

async def test_qod_patch(client):
    """Test case for qod_patch

    
    """
    params = [('repeat_after', 30),
                    ('authors', None),
                    ('title', 'title_example'),
                    ('private', False),
                    ('language', 'en'),
                    ('sfw', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/qod',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_qod_put(client):
    """Test case for qod_put

    
    """
    params = [('repeat_after', 30),
                    ('authors', None),
                    ('title', 'title_example'),
                    ('private', False),
                    ('language', 'en'),
                    ('sfw', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/qod',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

