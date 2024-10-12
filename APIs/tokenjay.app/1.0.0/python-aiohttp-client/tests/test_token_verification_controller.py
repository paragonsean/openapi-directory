# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_response import CheckResponse
from openapi_server.models.genuine_token import GenuineToken


pytestmark = pytest.mark.asyncio

async def test_check_token(client):
    """Test case for check_token

    Check a token verification
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/tokens/check/{token_id}/{token_name}'.format(token_id='token_id_example', token_name='token_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_blocked(client):
    """Test case for list_blocked

    Lists all blocked tokens
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/tokens/listBlocked',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_genuine(client):
    """Test case for list_genuine

    Lists all genuine tokens known
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/tokens/listGenuine',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

