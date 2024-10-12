# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ssh_key_with_user import SSHKeyWithUser


pytestmark = pytest.mark.asyncio

async def test_get_v3_keys_id(client):
    """Test case for get_v3_keys_id

    Get single ssh key by id. Only available to admin users
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/keys/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

