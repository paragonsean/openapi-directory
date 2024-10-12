# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.test_echo import TestEcho
from openapi_server.models.test_validate import TestValidate


pytestmark = pytest.mark.asyncio

async def test_echo(client):
    """Test case for echo

    Echo text
    """
    params = [('text', 'ok')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/test',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate(client):
    """Test case for validate

    Validate input
    """
    params = [('id', 123),
                    ('tag', ['tag_example'])]
    headers = { 
        'Accept': 'application/json',
        'user_agent': 'user_agent_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/test/validate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

