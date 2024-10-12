# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_v20_login_get(client):
    """Test case for api_v20_login_get

    
    """
    params = [('password', 'password_example'),
                    ('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/login',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

