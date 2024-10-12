# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_password_forgotten_0(client):
    """Test case for get_password_forgotten_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/password_forgotten',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_password_forgotten_key_0(client):
    """Test case for get_password_forgotten_key_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/password_forgotten/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_password_forgotten_0(client):
    """Test case for post_password_forgotten_0

    
    """
    params = [('login', 'login_example'),
                    ('drop_tokens', 'drop_tokens_example')]
    headers = { 
        'tester_pass': 'tester_pass_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/password_forgotten',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_password_forgotten_key_0(client):
    """Test case for post_password_forgotten_key_0

    
    """
    params = [('pass', '_pass_example'),
                    ('pass2', 'pass2_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/password_forgotten/{key}'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

