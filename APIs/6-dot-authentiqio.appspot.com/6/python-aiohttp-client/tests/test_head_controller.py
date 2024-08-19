# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_key_pkhead_0(client):
    """Test case for key_pkhead_0

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='HEAD',
        path='/key/{pk}'.format(pk='pk_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sign_retrieve_head_0(client):
    """Test case for sign_retrieve_head_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/scope/{job}'.format(job='job_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

