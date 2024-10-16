# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ssh_key_detail import SshKeyDetail


pytestmark = pytest.mark.asyncio

async def test_get_all_ssh_keys(client):
    """Test case for get_all_ssh_keys

    Overview of SSH keys
    """
    params = [('skip', 56),
                    ('take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/ssh',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

