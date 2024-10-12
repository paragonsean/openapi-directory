# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_cipher_use_entity import UserCipherUseEntity


pytestmark = pytest.mark.asyncio

async def test_get_user_cipher_uses(client):
    """Test case for get_user_cipher_uses

    List User Cipher Uses
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/user_cipher_uses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

